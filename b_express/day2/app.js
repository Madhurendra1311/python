const express = require('express')

const app = express()

app.use(express.json())
app.use(express.urlencoded({extended: false}))

// middleware
app.use((req, res, next) => {
    console.log(`${req.method} = ${req.url}`)
    next()
})

const users = [
    {name: 'rahul', age: 20},
    {name: 'manoj', age: 21},
    {name: 'sohan', age: 22}
]

const posts = [
    {title: 'my favorite food'},
    {title: 'my favorite games'}
]

app.get('/', (req, res) => {
    res.send({
        msg: "Hello World",
        user: { }
    })
})

app.post('/', (req, res) => {
    const user = req.body
    users.push(user)
    console.log(req.body)
    res.status(201).send('Created User')
})

app.get('/users', (req, res) => {
    res.status(200).send(users)
})

app.get('/users/:name', (req, res) => {
    const { name } = req.params
    const user = users.find((user) => user.name === name)
    if(user){
        res.status(200).send(user)
    }else{
        res.status(404).send('Not Found')
    }
})

app.get('/posts', (req, res) => {
    console.log(req.query)
    const { title } = req.query
    if(title){
        const post = posts.find((post) => post.title === title)
        if(post){
            res.status(200).send(post)
        }else{
            res.status(404).send('Not Found')
        }
    }
})

function validateAuthToken(req, res, next){
    console.log('Inside validate Auth Token')
    const {authorization} = req.headers
    if(authorization && authorization === '123'){
        next()
    }else{
        res.status(403).send({msg: 'Forbidden, Invalid Credential'})
    }
}

app.post('/posts',validateAuthToken, (req, res) => {
    const post = req.body
    console.log(post)
    posts.push(post)
    res.status(201).send(post)
})

// app.post('/posts', (req, res) => {
//     const {authorization} = req.headers
//     if(authorization && authorization === '123'){
//         const post = req.body
//         console.log(post)
//         posts.push(post)
//         res.status(201).send(post)
//     }else{
//         res.status(403).send('Forbidden')
//     }
// })

app.listen(3000, () => {
    console.log('Server is running on port 3000')
})