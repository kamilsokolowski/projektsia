if (process.env.NODE_ENV !== 'production') {
  require('dotenv').config()
}
const express = require('express');
const bodyParser = require('body-parser');
const passport = require('passport')
const bcrypt = require('bcrypt')
const flash = require('express-flash')
const session = require('express-session')
const { check, validationResult, sanitizeQuery, body } = require('express-validator');
const app = express();
const urlencodedParser = bodyParser.urlencoded({ extended: false });
var http = require('http');
const { Server } = require('tls');

const initializePassport = require('./passport-config');
const { get } = require('superagent');
initializePassport(
  passport,
  email => users.find(user => user.email=== email),
  id => users.find(user => user.id === id)
)
const users = []

app.use(
    express.urlencoded({
      extended: true
    })
  )

app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: false }))
app.use(flash())
app.use(session({
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false
}))
app.use(passport.initialize())
app.use(passport.session())
app.use('/assets', express.static('assets'));
app.use(express.json());

var api_options = {
    host: 'localhost',
    port: 8000,
    path: '',
    method: 'GET',
    headers: '',
    body: ''
};

app.get('', (req, resp) => {
  if (!req.isAuthenticated()) {
    api_options.path = '/api/zgloszenia/'
    api_options.method = 'GET'
    callback = (response) => {
        var api_response = '';

        response.on('data', (chunk) => {
            api_response += chunk;
        });
        
        response.on('end', () => {
            var api_json = JSON.parse(api_response);
            console.log(api_json)
            resp.render('index', {'news_list' : api_json.reverse().slice(0,4)});
        });

        response.on('error', () =>{
            console.error('/list-incidents error');
            return resp.render('index');
        });
      }
     
    http.request(api_options, callback).end();
  }
  else{
    api_options.path = '/api/zgloszenia/'
    api_options.method = 'GET'
    callback = (response) => {
      var api_response = '';

      response.on('data', (chunk) => {
          api_response += chunk;
      });
      
      response.on('end', () => {
          var api_json = JSON.parse(api_response);
          console.log(api_json)
          resp.render('index-logged', {'news_list' : api_json.reverse().slice(0,4)});
      });

      response.on('error', () =>{
          console.error('/list-incidents error');
          return resp.render('index-logged',{ name: req.user.name });
      });
    }
   
  http.request(api_options, callback).end();
  }
});

app.get('/', (req, resp) => {
  if (!req.isAuthenticated()) {
    api_options.method = 'GET'
    return resp.render('index');
  }
  else{
    api_options.method = 'GET'
    return resp.render('index-logged',{ name: req.user.name });
  }
});

app.get('/list-incidents',  (req, resp) => {
  if (!req.isAuthenticated()) {
    api_options.method = 'GET'
    api_options.path = '/api/zgloszenia/'
    callback = (response) => {
       var api_response = '';

       response.on('data', (chunk) => {
           api_response += chunk;
       });
     
       response.on('end', () => {
           var api_json = JSON.parse(api_response);
           return resp.render('news', {'news_list' : api_json});
       });

       response.on('error', () =>{
           console.error('/list-incidents error');
           return resp.render('index');
       });
     }
     
   http.request(api_options, callback).end();
    }
    else{
      api_options.method = 'GET'
      api_options.path = '/api/zgloszenia/'
      callback = (response) => {
         var api_response = '';
  
         response.on('data', (chunk) => {
             api_response += chunk;
         });
       
         response.on('end', () => {
             var api_json = JSON.parse(api_response);
             return resp.render('news-logged', {'news_list' : api_json});
         });
  
         response.on('error', () =>{
             console.error('/list-incidents error');
             return resp.render('index-logged');
         });
       }
       
     http.request(api_options, callback).end();
      } 
    
});

app.get('/contact', (req, resp) => {
  if (!req.isAuthenticated()) {
    api_options.method = 'GET'
    return resp.render('contact')
  }
  else{
    api_options.method = 'GET'
  return resp.render('contact-logged')
  }
});


app.get('/details/:id', (req, resp) => {
  if (req.isAuthenticated()) {
    api_options.method = 'GET'
    api_options.path = '/api/zgloszenia/'+req.params.id+'/'

    callback = (response) => {
        var api_response = '';

        response.on('data', function (chunk) {
          api_response += chunk;
        });
      
        response.on('end',  () => {
          var api_json = JSON.parse(api_response);
          return resp.render('details-logged', {details: api_json})
        });

        response.on('error', () => {
            console.error("/details/:id/ error")
            return resp.rendnav.ejs('index-logged');
        });
      }
      
    http.request(api_options, callback).end();
  }
  else{
    api_options.method = 'GET'
    api_options.path = '/api/zgloszenia/'+req.params.id+'/'
  
    callback = (response) => {
        var api_response = '';
  
        response.on('data', function (chunk) {
          api_response += chunk;
        });
      
        response.on('end',  () => {
          var api_json = JSON.parse(api_response);
          return resp.render('details', {details: api_json})
        });
  
        response.on('error', () => {
            console.error("/details/:id/ error")
            return resp.rendnav.ejs('index');
        });
      }
      
    http.request(api_options, callback).end();
  }
});

app.get('/form', (req, resp) => {
  if (req.isAuthenticated()) {
    api_options.method = 'GET'
  return resp.render('form');
  }
  else{
    api_options.method = 'GET'
  return resp.redirect('/');
  }
});

app.post('/form', (req, resp) => {

     data = JSON.stringify({
        "tytul_zgloszenia": req.body.title,
        "nick": req.body.nickname,
        "rodzaj": "None",
        "sciezka_do_pliku": 'temp',
        "latitude": req.body.latitude,
        "longitude": req.body.longtiude,
        "data_czas": "2020-12-12T12:12:00Z",
        "akceptacja": 0, // do zmiany pozniej na 0 żeby akceptować z poziomu administratora
        "opis": req.body.opis
    });

    api_options.path = '/api/zgloszenia/'
    api_options.method = 'POST'
    api_options.headers = {
        'Content-Type': 'application/json',
        'Content-Length': data.length
      }

    const requ = http.request(api_options, res => {
        console.log(`statusCode: ${res.statusCode}`)
      
        res.on('data', d => {
          process.stdout.write(d)
        });
      })
      
      requ.on('error', error => {
        console.error(error)
      })
      
    requ.write(data);
    resp.render('form');
    return requ.end();
    
});

app.get('/admin-panel/login', (req, resp) => {
    api_options.method = 'GET'
    
    return resp.render('login-panel');
});

app.post('/admin-panel/login',  checkNotAuthenticated, passport.authenticate('local', {
  successRedirect: '/',
  failureRedirect: '/admin-panel/login',
  failureFlash: true
}))

app.get('/register', (req, res) => {
    api_options.method = 'GET'
    res.render('register')
})

app.get('/admin-panel', (req, resp) => {
    api_options.method = 'GET'
    api_options.path = '/api/zgloszenia/'
  
    callback = (response) => {
        var api_response = '';
  
        response.on('data', function (chunk) {
          api_response += chunk;
        });
      
        response.on('end',  () => {
          var api_json = JSON.parse(api_response);
          return resp.render('admin-panel', {details: api_json})
        });
  
        response.on('error', () => {
            console.error("error")
            return resp.rendnav.ejs('index');
        });
      }
      
    http.request(api_options, callback).end();
});

app.get('/admin-panel/acc/:id', (req, resp) => {
  api_options.method = 'GET'
  api_options.path = '/api/zgloszenia/'+req.params.id+'/'
  var api_json = {};
  
    callback = (response) => {
        var api_response = '';
  
        response.on('data', function (chunk) {
          api_response += chunk;
        });
      
        response.on('end',  () => {
          api_json = JSON.parse(api_response);

          api_options.method = 'PUT'
          api_options.path = '/api/zgloszenia/'+req.params.id+'/'
          api_json["akceptacja"]=1;
          d = JSON.stringify(api_json);
          api_options.headers = {
            'Content-Type': 'application/json',
            'Content-Length': d.length
          }
          
            
          rr = http.request(api_options);
          rr.write(d);
          rr.end();
          return resp.redirect("/admin-panel")
        });
  
        response.on('error', () => {
            console.error("error")
            return resp.rendnav.ejs('index');
        });
      }
  
    http.request(api_options, callback).end();

    
});

app.get('/admin-panel/ref/:id', (req, resp) => {
  api_options.method = 'GET'
  api_options.path = '/api/zgloszenia/'+req.params.id+'/'
  var api_json = {};
  
    callback = (response) => {
        var api_response = '';
  
        response.on('data', function (chunk) {
          api_response += chunk;
        });
      
        response.on('end',  () => {
          api_json = JSON.parse(api_response);

          api_options.method = 'PUT'
          api_options.path = '/api/zgloszenia/'+req.params.id+'/'
          api_json["akceptacja"]=3;
          d = JSON.stringify(api_json);
          api_options.headers = {
            'Content-Type': 'application/json',
            'Content-Length': d.length
          }
          
            
          rr = http.request(api_options);
          rr.write(d);
          rr.end();
          return resp.redirect("/admin-panel")
        });
  
        response.on('error', () => {
            console.error("error")
            return resp.rendnav.ejs('index');
        });
      }
  
    http.request(api_options, callback).end();

    
});

app.get('/admin-panel/ref/:id', (req, resp) => {
  
});

app.get('/table', (req, resp) => {
    api_options.method = 'GET'
    return resp.render('table')
});

app.post('/register', urlencodedParser, [
    check('username')
        .isLength({ min: 1 })
        .withMessage('Nazwa użytkownika jest wymagana.'),
    check('email')
        .isLength({ min: 1 })
        .withMessage('Email jest wymagany.')
        .isEmail().withMessage('Prosimy o wprowadzenie poprawnego adresu e-mail'),
    check('name')
        .isLength({ min: 1 })
        .withMessage('Imię jest wymagane.'),
    check('surname')
        .isLength({ min: 1 })
        .withMessage('Nazwisko jest wymagane.'),
    check('password')
        .isLength({ min: 1 })
        .withMessage('Wymagane jest hasło.'),
    check('password1')
        .isLength({ min: 1 })
        .withMessage('Pole potwierdź hasło jest wymagane.')
        .exists()
        .custom((value, { req }) => value === req.body.password)
        .withMessage('Hasła muszą być identyczne.')
], async (req, resp) => {
        const errors = validationResult(req)
        if (!errors.isEmpty()) {
            // return res.status(422).jsonp(errors.array())
            const alert = errors.array()
            resp.render('register', {
                alert
            })
            
            return requ.end();
        }
        data = JSON.stringify({
          "nick": req.body.username,
          "imie": req.body.name,
          "nazwisko": req.body.surname,
          "organizacja": "11",
          "uprawnienia": 1,
          "liczba_zgloszen": 1,
          "haslo": req.body.password,
     });
     const hashedPassword = await bcrypt.hash(req.body.password, 10)
     users.push({
      id: Date.now().toString(),
      name: req.body.name,
      email: req.body.email,
      password: hashedPassword
    })
     api_options.path = '/api/uzytkownik/'
     api_options.method = 'POST'
     api_options.headers = {
         'Content-Type': 'application/json',
         'Content-Length': data.length
       }
  
     const requ = http.request(api_options, resp => {
         console.log(`statusCode: ${resp.statusCode}`)
       
         resp.on('data', d => {
           process.stdout.write(d)
         });
       })
       
       requ.on('error', error => {
         console.error(error)
       })
       
     requ.write(data);
     resp.redirect('/');
     return requ.end();
});


// Standard 404 error.
app.get('*', (req, resp) => {
    api_options.method = 'GET'
    return resp.redirect('/');
});

app.post('/logout', (req, res) => {
  req.logOut()
  res.redirect('/login')
})

function checkNotAuthenticated(req, res, next) {
  if (req.isAuthenticated()) {
    return res.redirect('/')
  }
  next()
}

app.listen(3000);
