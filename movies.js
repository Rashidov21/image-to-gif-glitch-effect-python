let movies = ['tt0816692', 'tt0110413', 'tt0172495', 'tt1853728', 'tt1345836', 'tt0361748']
let getMovieBtn = document.getElementById('get')
    // Informartion blocks
let poster = document.getElementById('poster')
let title = document.getElementById('title')
let actors = document.getElementById('actors')
let country = document.getElementById('country')
let director = document.getElementById('director')
let genre = document.getElementById('genre')
let year = document.getElementById('year')
let rating = document.getElementById('rating')




function getMovie() {
    let randomMovie = Math.floor(Math.random() * movies.length)
    let movie = movies[randomMovie]
    let url = `http://www.omdbapi.com/?i=${movie}&apikey=fb78af15`
    const xhr = new XMLHttpRequest();
    xhr.open('POST', url)
    xhr.addEventListener('load', () => {
        const response = JSON.parse(xhr.responseText)
        poster.src = response.Poster;
        title.innerHTML = response.Title;
        actors.innerHTML = response.Actors;
        country.innerHTML = response.Country;
        director.innerHTML = response.Director;
        genre.innerHTML = response.Genre;
        year.innerHTML = response.Year;
        rating.innerHTML = response.imdbRating;
    });
    // commnet
    xhr.addEventListener('error', () => {
        console.log('error')
    });
    xhr.send();
}
getMovieBtn.addEventListener("click", () => {
    getMovie()
})
fetch('https://dummyapi.io/data/v1/post?limit=10')
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log(data);
    });