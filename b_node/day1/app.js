const express = require('express')
const app = express()

let users = [
    {
        username: "ram",
        email: "ram@gmail.com",
        age: 20
    }
];

app.get('/getuser/:username', (req, res) => {
    const username = req.params.username
    const getUser = users.find(user => {
        return (user.username === username)
    })
    if (getUser) {
        res.status(200).json(getUser)
    }
    else {
        res.status(404).json({ error: "Erorr Fetching the User" })
    }
})

app.post('/adduser', (req, res) => {
    const username = req.query.username
    const email = req.query.email
    const age = req.query.age
    const user = { username, email, age }
    users.push(user);
    res.status(200).json({ message: "Student Added Successfully" })
})

app.delete('/deleteuser/:username', (req, res) => {
    const username = req.params.username
    const userIndex = users.findIndex(user => {
        return (user.username === username)
    })
    if (userIndex >= 0) {
        users.splice(userIndex, 1);
        res.status(200).json({ message: "Delete Successful" })
    }
    else {
        res.status(404).json({ error: "Erorr Fetching the User" })
    }
})

app.get('/*', (req, res) => {
    res.status(404).send('Error!')
})
app.post('/*', (req, res) => {
    res.status(404).send('Error!')
})
app.put('/*', (req, res) => {
    res.status(404).send('Error!')
})



app.listen(5000, () => {
    console.log('The server is up and running')
})