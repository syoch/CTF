defineHandler({
  onEnter(log, args, state) {
    console.log(
      `CreateFileA(${args[0].readUtf8String()}, ${args[1]}, ${args[2]}, ${args[3]}, ${args[4]}, ${args[5]}, ${args[6]})`,
    );
  },

  onLeave(log, retval, state) {
    console.log(`CreateFileA returned ${retval}`);
  },
});
