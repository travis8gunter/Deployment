console.log("connected")

let gameWrapper = document.querySelector("section");
let inputTitle = document.querySelector("#input-title-name");
let inputGenre = document.querySelector("#input-genre");
let inputRating = document.querySelector("#input-rating");
let inputMultiplayer = document.querySelector("#input-multiplayer");
let inputPrice = document.querySelector("#input-price");
let inputEmail = document.querySelector("#input-email-login");
let inputPassword = document.querySelector("#input-password-login");

let saveGameButton = document.querySelector("#save-game-button");

if (!gameWrapper || !inputTitle || !inputGenre || !inputRating || !inputMultiplayer || !inputPrice || !saveGameButton) {
    console.error("Error: One or more required DOM elements are missing.");
}

let editId = null;

function saveGameToServer() {
    let data = "title=" + encodeURIComponent(inputTitle.value);
    data += "&genre=" + encodeURIComponent(inputGenre.value);
    data += "&rating=" + encodeURIComponent(inputRating.value);
    data += "&multiplayer=" + encodeURIComponent(inputMultiplayer.value);
    data += "&price=" + encodeURIComponent(inputPrice.value);

    let URL = "http://localhost:8080/games";
    let method = "POST";
    if(editId) {
        URL = "http://localhost:8080/games/" + editId;
        method = "PUT";
    }

    fetch(URL, {
        method: method,
        body: data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }).then(function(response) {
        console.log("New game Saved!", response);
        gameWrapper.textContent = "";
        loadGameFromServer();
    })

    inputTitle.value = "";
    inputGenre.value = "";
    inputRating.value = "";
    inputMultiplayer.value = "";
    inputPrice.value = "";
    
    editId = null;
}

function addGame(data) {
    try {
        if (!data || !data.title || !data.genre || !data.rating || !data.multiplayer || !data.price) {
            //console.log(data)
        }

        let gameTitle = document.createElement("h5");
        let gameGenre = document.createElement("h5");
        let gameRating = document.createElement("h5");
        let gameMultiplayer = document.createElement("h5");
        let gamePrice = document.createElement("h5");
        let editButton = document.createElement("button");
        let deleteButton = document.createElement("button");

        gameTitle.textContent = "Title: " + data.title;
        gameGenre.textContent = "Genre: " + data.genre;
        gameRating.textContent = "My Rating: " + data.rating;
        gameMultiplayer.textContent = data.multiplayer == 1 ? "Multiplayer" : "Not Multiplayer";
        gamePrice.textContent = "$" + data.price;
        editButton.textContent = "Edit";
        deleteButton.textContent = "Delete";

        gameWrapper.appendChild(gameTitle);
        gameWrapper.appendChild(gameGenre);
        gameWrapper.appendChild(gameRating);
        gameWrapper.appendChild(gameMultiplayer);
        gameWrapper.appendChild(gamePrice);
        gameWrapper.appendChild(editButton);
        gameWrapper.appendChild(deleteButton);
        gameWrapper.appendChild(document.createElement("hr"));

        editButton.onclick = function() {
            inputTitle.value = data.title;
            inputGenre.value = data.genre;
            inputRating.value = data.rating;
            inputMultiplayer.value = data.multiplayer;
            inputPrice.value = data.price;
            
            editId = data.id;
        };

        deleteButton.onclick = function() {
            if (confirm("Do you want to delete this item?")) {
                deleteGameFromServer(data.id);
                console.log("Item deleted.");
            } else {
                console.log("Action canceled.");
            }
        };
    } catch (error) {
        console.error("Error in addGame:", error.message);
    }
}

function loadGameFromServer() {
    fetch("http://localhost:8080/games")
    .then(function(response) {
        response.json().then(function(data){
            console.log(data);
            let games = data;
            games.forEach(addGame);
        })
    }).catch(function(error) {
        console.error("Network error:", error);
    });
}

saveGameButton.onclick = saveGameToServer;       
loadGameFromServer();

function deleteGameFromServer(id) {
    let URL = "http://localhost:8080/games/" + id;

    fetch(URL, {
        method: "DELETE"
    }).then(function(response) {
        if (response.ok) {
            console.log("Game Deleted!", response);
            gameWrapper.textContent = "";  
            loadGameFromServer();  
        } else {
            console.error("Error deleting game");
        }
    }).catch(function(error) {
        console.error("Network error:", error);
    });
}





const apiUrl = window.location.protocol === 'file:'
  ? 'http://localhost:8080' // Local API server during development
  : ''; // Production API

Then, you will remove any reference to 'http://localhost:8080' within your code and replace it with apiUrl.

In your python file make sure your run function looks like this:

def run():
    app.run(port=8080, host='0.0.0.0')