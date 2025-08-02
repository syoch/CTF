let array = [];
array.push(new WeakRef({ a: 0 }));

console.log("log", array, array.map(x => x.deref()));

setTimeout(() => {
  globalThis.gc(); // now it will be collected
  console.log("log", array, array.map(x => x.deref()));
}, 100);
