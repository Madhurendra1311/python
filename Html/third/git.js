function getDetails() {
    var xhr = new XMLHttpRequest()
    var query = document.getElementById('input').value
    xhr.open('GET', "https://api.github.com/search/users?q=" + query)
    xhr.send()

    xhr.onload = function () {
        var data = JSON.parse(this.response)
        displayResults(data)
    }
}

function displayResults(data) {
    var result = document.getElementById('res')
    result.innerHTML = ""
    var count = data.total_count;

    var p = document.createElement('p')
    p.innerText = count + "users found"

    var ol = document.createElement('ol')
    var items = data.items
    for (var i = 0; i < items.length; i++) {
        var li = document.createElement('li')

        var name = document.createElement('p')
        name.innerText = items[i].login

        var img = document.createElement('img')
        img.src = items[i].avatar_url
        li.append(name, img)
        ol.append(li)
    }
    result.append(p, ol)
}

var btn = document.getElementById("get")

btn.addEventListener('click', getDetails)