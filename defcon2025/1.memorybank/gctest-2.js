class User {
  constructor(username) {
    this.username = username;
  }
}

class UserRegistry {
  constructor() {
    this.users = [];
  }
  addUser(user) {
    this.users.push(new WeakRef(user));
  }
  getUserByUsername(username) {
    console.log(this.users.map(x => x.deref()));
    for (let user of this.users) {
      user = user.deref();
      if (!user) continue;
      if (user.username === username) {
        return user;
      }
    }
    return null;
  }
}
const users = new UserRegistry();

function init() {
  users.addUser(new User("bank_manager"));
}

async function user() {
  globalThis.gc();
  users.getUserByUsername("bank_manager");
}

async function main() {
  init();
  setTimeout(async () => {
    await user();
  }, 10);
}

main()