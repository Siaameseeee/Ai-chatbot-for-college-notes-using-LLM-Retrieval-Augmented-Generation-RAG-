async function send(){

const input = document.getElementById("input");
const text = input.value;

const messages = document.getElementById("messages");

messages.innerHTML += `<div class="user">You: ${text}</div>`;

const res = await fetch("/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body: JSON.stringify({message:text})
});

const data = await res.json();

messages.innerHTML += `<div class="bot">AI: ${data.reply}</div>`;

input.value="";
}
