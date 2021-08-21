M.AutoInit();

let addPost = document.getElementById('addPost')
let getPost = document.getElementById('getPost')
let posts = document.getElementById('posts')
function getPosts(){
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts/')
    xhr.addEventListener('load', ()=>{
        const response = JSON.parse(xhr.responseText)
        console.log(response)
        for(let i = 0; i < response.length; i++){
            let post = response[i]
            let box = document.createElement("div")
            box.innerHTML = `<h5>${post.title}</h5><p>${post.body}</p>`;
            let firstCh = posts.firstChild;
            posts.insertBefore(box, firstCh)
        }
    });
    xhr.addEventListener('error', ()=>{
        console.log('error')
    });
    xhr.send();
}
getPost.addEventListener("click", ()=>{
    getPosts()
})
////////////////////////////////////////////////
function createPost(body,cb){
    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://jsonplaceholder.typicode.com/posts/')
    xhr.addEventListener('load', ()=>{
        const response = JSON.parse(xhr.responseText)
        cb(response)
    });
    xhr.addEventListener('error', ()=>{
        console.log('error')
    });
    xhr.send(JSON.stringify(body));
}

addPost.addEventListener("click", (e)=>{
    const newPost = {
        title:'Qale ishla',
        body:"Nima gap",
        userId:1
    }
    createPost(newPost, (response)=>{
        console.log(response)
    })
})
fetch('https://jsonplaceholder.typicode.com/posts/1')
    .then((response) => response.json())
    .then((json) => console.log(json));