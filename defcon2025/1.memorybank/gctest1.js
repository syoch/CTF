async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function user(wref) {
  await sleep(0);
  globalThis.gc();
  // するとwref.deref()の返り値はundefinedになる
  console.log(wref.deref()); // undefined
}

async function main() {
  let obj = { name: "object 1" }; // objにオブジェクト1を代入

  const wref = new WeakRef(obj);

  console.log(wref.deref()); // { name: "object 1" };

  // オブジェクト1への（弱ではない）参照を無くす
  obj = null;
  setTimeout(() => {
    user(wref);
  }, 10);
}

main();