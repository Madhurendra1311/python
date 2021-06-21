const express = require('express')
const app = express()

app.get('/', (req, res) => {
    res.status(200, { 'Content-Type': 'text/html' })
    res.write(
        '<html><body><h1>Welcome to Innominds!</h1></body></html>'
    )
    res.end();
})

app.get('/home', (req, res) => {
    res.status(200)
    res.redirect('/')
    res.end();
})

app.get('/search', (req, res) => {
    res.status(200)
    res.redirect('https://www.google.com')
    res.end();
})

app.listen(3000, () => {
    console.log('The server is up and running')
})