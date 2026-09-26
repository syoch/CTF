const ignoreSymbols = [];
const interestedSymbols = [];
const inspectSymbols = [];

const inModuleGeneric = (mod) => (addr) =>
  mod.base.compare(addr) < 0 && addr.compare(mod.base.add(mod.size)) < 0;

const inModule = inModuleGeneric(Process.mainModule);
console.log(
  `Target module: ${Process.mainModule.name} (${Process.mainModule.base} - ${Process.mainModule.base.add(Process.mainModule.size)})`,
);

(() => {
  const mod = Process.getModuleByName("ws2_32.dll");
  // send
  {
    const fn = mod.findExportByName("send");
    Interceptor.attach(fn, {
      onEnter(args) {
        console.log(
          `Entered send with arguments: ${args[0]}, ${args[1]}, ${args[2]}`,
        );
        console.log(hexdump(args[1], { length: args[2].toInt32() }));
      },
      onLeave(retval) {
        console.log(`Leaving send with return value: ${retval}`);
      },
    });
  }

  // recv
  {
    const fn = mod.findExportByName("recv");
    Interceptor.attach(fn, {
      onEnter(args) {
        console.log(
          `Entered recv with arguments: ${args[0]}, ${args[1]}, ${args[2]}`,
        );
      },
      onLeave(retval) {
        console.log(`Leaving recv with return value: ${retval}`);
        if (retval.toInt32() > 0) {
          console.log(hexdump(this.context.rdx, { length: retval.toInt32() }));
        }
      },
    });
  }
})();

// attach to all interested symbols
if (0)
  inspectSymbols
    .map(({ offset, tag }) => ({
      addr: Process.mainModule.base.add(offset),
      tag,
    }))
    .forEach(({ addr, tag }) => {
      console.log(`Attaching to ${tag}`);
      Interceptor.attach(addr, {
        onEnter(args) {
          console.log(
            `Entered ${tag} with arguments: ${args[0]}, ${args[1]}, ${args[2]}, ${args[3]}, ${args[4]}`,
          );

          if (tag === "CallHash5" && args[2] != 0) {
            // Dump the structure pointed by args[2] with 64 bytes
            console.log(`Dumping structure at ${args[2]}:`);
            console.log(hexdump(args[2], { length: 64 }));
          }
        },
        onLeave(retval) {
          console.log(`Leaving ${tag} with return value: ${retval}`);
        },
      });
    });

if (0)
  Process.enumerateThreads().map((t) => {
    Stalker.follow(t.id, {
      events: {
        call: true, // CALL instructions: yes please
        // Other events:
        ret: false, // RET instructions
        exec: false, // all instructions: not recommended as it's
        //                   a lot of data
        block: false, // block executed: coarse execution trace
        compile: false, // block compiled: useful for coverage
      },
      onReceive(events) {
        let res = Stalker.parse(events, { annotate: true });
        for (let evt of res) {
          if (evt[0] == "block") {
            let begin = ptr(evt[1]).toInt32();
            let end = ptr(evt[2]).toInt32();
            if (inModule(ptr(begin))) {
              console.log(`block at ${evt[1]} --> ${evt[2]}`);
            }
          } else if (evt[0] == "call") {
            const caller = ptr(evt[1]);
            const callee = ptr(evt[2]);
            if (inModule(caller) || inModule(callee)) {
              const offset = callee.sub(Process.mainModule.base);
              const ignored = ignoreSymbols.includes(offset.toInt32());
              const interested = interestedSymbols.includes(offset.toInt32());
              if (!ignored) {
                console.log(
                  `call from ${caller} to ${callee} ${interested ? "(interested)" : ""}`,
                );
              }
            }
          } else {
            console.log(`Unknown event: ${JSON.stringify(evt)}`);
          }
        }
      },
    });
  });
