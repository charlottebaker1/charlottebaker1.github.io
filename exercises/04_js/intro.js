function sayHello() {
    console.log('Hello, World!');
}
const btnClickMe = document.getElementById('btn-click-me');
console.log(btnClickMe);
btnClickMe.onclick = sayHello();
