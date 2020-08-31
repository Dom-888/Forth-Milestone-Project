# [The Yellow Dice](https://the-yellow-dice.herokuapp.com/)

An eCommerce website for tabletop games, made with Django

!["Responsive Representation"](static/images/misc/responsive-representation.png "Responsive Representation")

## Table of Contents
1. [**UX**](#ux)
    - [**User Goals**](#user-goals)
    - [**User Stories**](#user-stories)
    - [**Design Choices**](#design-choices)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)
    - [**Tested Devices**](#tested-devices)
    - [**Simulated Devices**](#simulated-devices)
    - [**Manual Testing**](#manual-testing)
    - [**Validation Services**](#validation-services)
    - [**Bugs Discovered**](#bugs-discovered)

### 

6. [**Deployment**](#deployment)
    - [**How to run this project locally**](#how-to-run-this-project-locally)
    - [**Heroku Deployment**](#heroku-deployment)

7. [**Credits**](#credits)
    - [**Code**](#code)
    - [**Media**](#media)
    - [**Acknowledgments**](#acknowledgments)

8. [**Disclaimer**](#disclaimer)



## UX

### User Goals

| As a user of the site, I want to be able to:                                                                     | The Yellow Dice meets these needs by:                                                                           |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Easily understand how to use the site.                                                                           | Having a clear user interface and providing visual feedback to user actions.                                    |
| Choose between various categories of tabletop games.                                                             | Allowing to browse through 4 game categories: Board Games, Cards, Abstract and, Mash-Up.                        |
| Search the site for a specific feature or game element, for example cards or dice.                               | Having a search function that goes through the game title, its description and the items included in the box.   |
| Choose games similar to those I already know and have enjoyed.                                                   | Suggesting a list of similar games each time the user selects a game.                                           |
| Use the site from my smartphone as well as my tablet and my laptop.                                              | Being fully responsive, having been created following the mobile-first approach.                                |
| Register an account with my shipping details so that I don't have to re-enter them every time I make a purchase. | Providing a form in which to enter or modify relevant information.                                              |
| Make a one-time purchase with no need to register an account.                                                    | Making the account registration optional.                                                                       |
| Complete each purchase quickly and easily.                                                                       | Providing a minimal checkout page with no distractions that can divert the user's attention.                    |
| See my order history.                                                                                            | Providing a detailed list of orders placed.                                                                     |

### User Stories

- I'm a tabletop games enthusiast looking to expand my collection,
I already know all the most popular games and I am looking for a site with a large selection and that is up to date on the latest news.
In the _The Yellow Dice_ I have the ability to search for a specific game mechanic and I can see the exact contents of the game box before completing a purchase.
I generally use my PC to shop online, however I want to be able to browse new games anywhere with my phone.
I will probably buy again in the future and therefore I want to record my shipping details to speed up future purchases.

- I'm a casual gamer, I know the most popular tabletop games but I'm not an expert and I'm looking for something new to play.
Browsing the Mashup section of the _The Yellow Dice_ I discover _Clue: The Office Edition_, which is perfect for me as I'm familiar with _Cluedo_'s gameplay mechanics and I love _The Office_ TV series.
_The Yellow Dice_ allows me to complete the purchase without having to register an account as it is unlikely that I will purchase another game in the short term.

- I'm looking for a gift to buy for my grandchildren but I'm not a tech-savvy person and I need a simple site to use.
After landing on _The Yellow Dice_, the Site introduction confirms my idea that a tabletop game is the right choice.
The text is bigger than the average with a clean font and a good contrast between characters and background making it very easy to read.
After choosing the game, a pop-out message guides me to the checkout page,
here the buying process is simple and straightforward: there are no distracting elements on the page, I just have to fill the form and click on the large "Buy" Button.
Finally, a confirmation email assures me that the purchase was successful.

### Design Choices

#### Fonts  
All fonts are from [Google Fonts](https://fonts.google.com/).  
- _Roboto_: Site main font, it was chosen for its clear and straight design.  
- _Roboto Slab_: A more stylized version of Roboto, used in page headers.
- _Righteous_: Used in the logo, chosen for its distinctiveness.

#### Color Palette
The site uses light, pastel colors with good contrast between them.
- _Gold Yellow (#FFD700)_: Chosen to create the logo, also used to highlight the hovered navbar elements.
- _Sky Blue (#1F96F4)_: Used for the navbar, footer, and logo background, it was chosen to create a nice contrast with the yellow of the logo.
- _Light Gray (#E5E5E5)_: Used for the site background.
- _Dark Gray (#99999)_: Used for the placeholder text in forms and searchbar.  
- _Bootstrap Green (#5cb85c)_: Used for most of the buttons on the site.
- _Bootstrap Red (#d9534f)_: Used for the "remove from cart" buttons.

#### Icons  
All icons are from [Feather Icons](https://feathericons.com/).  
- _Cart Icon_: The cart icon is easily reachable from any part of the site, being placed in the right corner of the navbar, as it is conventionally used in this type of site and is where the user expects to find it.
- _Cart Operations_: Icons are used to manage cart operations (add item, change quantity, and delete item), with easily recognizable symbols that communicate their meaning in a more intuitive way than the written text. 
- _Site Navigation_: Icons have also been added to navigation buttons as visual clues to facilitate site navigation.
- _Social Media Icons_: Placed in the footer to give access to the 3 main social media: Facebook, Instagram, and Twitter.

### Wireframes  
  
The wireframes were created using [Figma](https://www.figma.com/) and can be found [here](https://www.figma.com/file/c22Y7U3hy37bp4gazuvnpb/Forth-Milestone-Project?node-id=0%3A1.)


## Features

### Existing Features

### Features Left to Implement

## Technologies Used
  
#### Languages  
- [HTML5](https://devdocs.io/html/)
- [CSS3](https://devdocs.io/css/) 
- [JavaScript](https://devdocs.io/javascript/)
- [Python](https://www.python.org/)

#### Frameworks  
- [Django](https://www.djangoproject.com/) to construct and render pages.
- [Bootstrap](https://getbootstrap.com/) to create the responsive design.  

#### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.  
- [Google Fonts](https://fonts.google.com/) to import the fonts used on the website.  
- [Feather Icons](https://feathericons.com/) to import the icons used on the website.  
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms. 
- [Gunicorn](https://pypi.org/project/gunicorn/) to aid in deployment of the Django project to heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) as Python imaging library to aid in processing image files to store in database.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.

#### Databases  
- [SQLite](https://www.sqlite.org/index.html) as development database.
- [PostgreSQL](https://www.postgresql.org/) as production database.  

#### Services
- [GitPod](https://www.gitpod.io/) was the main IDE in which the project was developed.  
- [Git](https://git-scm.com/) for version control during the development process.  
- [GitHub](https://github.com/) to host the project in a remote repository.  
- [Heroku](https://dashboard.heroku.com/apps) to deploy the project.  
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) to test responsiveness and quickly debug code.  
- [HTML Validator](https://validator.w3.org/) to test the HTML code.  
- [CSS Validator](https://jigsaw.w3.org/css-validator/) to test the CSS code.  
- [JSHint](https://jshint.com/) to test the JavaScript code.  
- [Python syntax checker](https://extendsclass.com/python-tester.html) to test the Python code.
- [Autoprefixer](https://autoprefixer.github.io/) to add prefixes in the CSS for cross-browser support.  
- [Figma](https://www.figma.com/) for wireframing.
- [Stripe](https://stripe.com/en-ie) as payment platform to validate and accept credit card payments securely.
- [AWS S3](https://aws.amazon.com/) to store images and static files.
- [BrowserStack](https://www.browserstack.com/) to test multiple devices and browsers.
- [Am I Responsive?](http://ami.responsivedesign.is/) to take the [screenshot](#open-trailer) placed at the beginning of this document. 

#### Software
- [Paint.net](https://www.getpaint.net/) to simple image manipulation.
- [Visual Studio Code](https://code.visualstudio.com/) for testing snippet of JS code.
- [Spyder](https://www.spyder-ide.org/) for testing snippet of Python code.  


## Testing  
  
### Tested Devices  
The website has been successfully tested with the following devices, plus all those simulated by the [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools).    
  

| Type       | Device                      | Browsers                     |  
| -----------|---------------------------- |------------------------------|  
| Laptop     | Asus FX753VD                | Chrome, Firefox, Edge, Opera |  
| Smartphone | Lenovo Moto G5S Plus        | Chrome, Firefox              |  
| Smartphone | Samsung Galaxy note 10 plus | Chrome                       |  
| Smartphone | Samsung Galaxy s9           | Chrome                       |  
| Smartphone | Samsung Galaxy a50          | Firefox Focus                |  
| Smartphone | Asus ZenFone 4 max          | Chrome                       |  
| Smartphone | Apple iPhone 7              | Safari                       |   

### Simulated Devices

[BrowserStack](https://www.browserstack.com/) was used to test the website on the following simulated devices:

| Type       | Device                      | Browsers |       
| -----------|---------------------------- |----------|  
| Smartphone | Galaxy Note 9               | Chrome   |  
| Tablet     | Galaxy Tab S6               | Chrome   |  
| Smartphone | iPhone 11                   | Safari   |  
| Tablet     | iPad Pro 11                 | Safari   |  
| Tablet     | iPad Air 2                  | Safari   |  

  
### Manual Testing
  
### Validation services  
  
### Bugs Discovered  

## Deployment

### How to run this project locally

In case you want to pull the code from my Github repository:  
1. Log in to Github,  

2. Follow [this](https://github.com/Dom-888/Forth-Milestone-Project) link to the project repository.  

3. In the repository page, click **Clone or download ▼**.  

4. To clone the repository using HTTPS, under "Clone with HTTPS", click the clipboard icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click **Use SSH**, then click the clipboard icon.  

5. Open Git Bash.  

6. Change the current working directory to the location where you want the cloned directory to be made.  

7. Type `git clone`, and then paste the URL you copied in Step 3.  

8. Install all required modules with the command:
```
pip -r requirements.txt.
```

9. Go on [Stripe](https://dashboard.stripe.com/register) and register a free account.

10. In the Stripe dashboard, click on **Get your test API keys** and copy both the Publishable Key and Secret Key. (Note that the Publishable Key can be committed to the repository without any problems, The Secret Key however must never be made public.)

11. In the project main directory create a file called `env.py`.

12. Inside the env.py file import os and create two variables: STRIPE_PUBLISHABLE_KEY and STRIPE_SECRET_KEY, assign them the respective strings taken from the Stripe dashboard.
The final content of your env.py should look like this:

```
import os

os.environ["STRIPE_PUBLISHABLE_KEY"] = "pk_test_..." 
os.environ["STRIPE_SECRET_KEY"] = "sk_test_..." 

````

13. You can now run the application with the command:
```
python manage.py runserver
```

14. The site can be visited at `http://127.0.0.1:8000/`

## Heroku Deployment

To deploy the project on Heroku, take the following steps:

1. Sign In on Heroku or create a new account

4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to the one closest to you, then click the "Create app" button.

3. Push the project to GitHub.

5. In the Heroku dashboard, click on resources and search for "Heroku Postgres" and click on **Provision**.

4. Go on [AWS](https://aws.amazon.com/) and create a free account.

5. [Set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) on [AWS](https://aws.amazon.com/), after creating the bucket you should be able to download a .csv file with 2 secret keys which you will need later.

6. Make a copy of the media folder of your project inside the bucket.

7. Create a new Gmail account or set up an existing one. In the Google account setting click on security and activate the 2-step verification. Return back in the security page and click on **App password**, you'll get a 16 character password which you'll need later. It is possible to use a provider other than Gmail, but the procedure will be different.

8. Go on [this](https://miniwebtool.com/django-secret-key-generator/) link and generate a new secret key for your Django app.

5. From the heroku dashboard of your newly created application, click on **Settings** -> **Reveal Config Vars** and set as the following:

| KEY                    | VALUE                                                                 |
|------------------------|-----------------------------------------------------------------------|
| AWS_ACCESS_KEY_ID      | <Same as the AWS .csv file>                                           |
| AWS_SECRET_ACCESS_KEY  | <Same as the AWS .csv file>                                           |
| DATABASE_URL           | <Automatically set by Heroku>                                         |
| DISABLE_COLLECTSTATIC  | 1                                                                     |
| EMAIL_HOST_PASS        | <The 16 character gmail password for apps>                            |
| EMAIL_HOST_USER        | <The new gmail address>                                               |
| SECRET_KEY             | <Your Django secret key>                                              |
| STRIPE_PUBLISHABLE_KEY | <Same as your env.py>                                                 |
| STRIPE_SECRET_KEY      | <Same as your env.py>                                                 |
| USE_AWS                | True                                                                  |
| DEVELOPMENT            | <Optional, without this variable, each error will return a 404 page.> |


10. Migrate the database models in your new database.

10. Create your superuser account in your new database.
  
9. In your heroku dashboard, click **Deploy**. Scroll down to **Manual Deploy**, select the master branch then click **Deploy Branch**.

10. Once the build is complete, click the **Open app** button. 
  
## Credits  
  
### Code  
  
### Media  
  
### Acknowledgments 

<br>  
  
#### Disclaimer  
  