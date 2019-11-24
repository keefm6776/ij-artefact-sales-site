#MODULE 9 (Full Stack Frameworks With Django) PROJECT - Code Institute Full Stack Developer Diploma
#E-Commerce Website (Artefact Sales)

[![Build Status](https://www.travis-ci.org/keefm6776/ij-artefact-sales-site.svg?branch=master)](https://www.travis-ci.org/keefm6776/ij-artefact-sales-site)

##Project purpose:
In this project, you'll build a full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a artefact/service.

Value provided: By authenticating on the site and paying for some of its services, users can advance their own goals. Before authenticating, the site makes it clear how those goals would be furthered by the site.

The site owner is able to make money by providing this set of services to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.

##BRIEF (CHOSEN PROJECT)
Build an auction place to sell historical artifacts, with the following goals:

1.  External user’s goal:   Find, learn about and acquire artifacts they are interested in

2.  Site owner's goal:      Earn money on selling the artifacts (the site owner is the seller)
    Potential features to include:

1.  Create an online store focused on selling unique historical artifacts,
    such as The Holy Grail to the highest bidder.

2.  Allow users to search for artifacts based on various fields.

3.  Allow users to see the price, image and other basic details about an artifact.

4.  Users would be able to learn about the historical details of each artifact,
    the culture it came from, the way it was created and its journey across different
    owners in the past.

    For example, you might want to include information about "events" that took place
    in the past and that one or more artifacts took place in, or originated from.

5.  Allow users to bid on items, or pay a higher price to purchase them immediately.
    Users have to be registered for this.

##Advanced potential feature (nice-to-have)

1.  Allow registered users to write reviews about the artifacts, only if they purchased them.

2.  Expand the search functionality to allow users to sort results based on price,
    age and other parameters in both ascending and descending order.

3.  Include pagination and/or other dynamic display actions using javascript.

4.  Use javascript polling to update the page whenever there's a new bid.

#CHOSEN PROJECT

##User Stories

Before Starting, I started to create some user stories:

1.	As a User I want to be able to search for artefacts that interest me, by their name or
    a particular era in history.
2.  As a User I want to be able to view the artefacts information including description,
    history and what era it is from.
3.	As a User I want to be able to purchase the artefact if I like it, or leave a bid
    if I am not willing to pay the price asked.
4.  As the site's owner I want to be able to manage the items on the site, adding them as
    they become available to me and to mark them as sold when they sell.
5.  As the sit's owner I want to be able to accept a bid that I deem acceptable for the item.

##Database Design

Before starting this project, I researched various e-commerce websites that are on the web, as mentioned in Credits -> Content, Below. I then set about drawing up a database schema for a relational database as per the project requirements.

UX
As part of the development process I mocked up wireframes of my recipe site before starting:

See my repository's file list:

.PDF .PDF

Which are located in the Wireframe directory.

Features
Features Left To Implement
Technologies Used
			1.	GITPOD	        -   All the HTML/CSS/JAVASCRIPT/PYTHON was edited using GITPOD.

			2.	HTML 5 		    -   The structure of the page has been created in HTML5.

			3.	CSS 3	        -   The pages were styled using SS3.

			4.	FLEXBOX	        -   Flexbox was used to centre buttons and titles.

			5.	FONT AWESOME    -   Font Awesome was used to provide the icons throughout the project, as required.

			6.  JAVASCRIPT      -   Javascript Was used by Materialize and JQuery, to operate and to initialise.
									Javascript was also used to provide an exit button on the view recipe form.

			7.  JQUERY 3.3.1    -   JQuery was used in the operation of menus.

			8.	BOOTSTRAP       -	I used Bootstrap to provide the base HTML for my site.  It also provided the grid
									feature for responsiveness, and glyphicons for use throughout.

			10. SQL LITE 3		-	I used SQL Lite as the relational databse to keep all the information required for this
									project to run.  This included :

			9.  Google Chrome Developer Tools - Used To Test While Developing, checking output and values during processing.
												Testing Functions during development, general tesing of website responsiveness

			10. Git/GitHub		-	Used for version control with regular commits.

			11. Heroku          -   Used to deploy the project.

Git Commits
I have made regular Git Commits during my project for version control and also to allow myself to go back if anything went wrong. I have pushed each of these commits to GitHub, so that the progress of my project can be reviewed. I folowed the steps provided by the GitHub site, which were:

			1.	I set up a page in GITPOD
			2.	In the terminal I typed "git init", to initialise the repository
			3.	To add files to be committed, I typed "git add ."
			4.  To check that these files were staged, I typed "git status" (staged files should be in green font)
			5.	To commit these to git, the command "git commit -m "messsage"", was used.  With a meaningful message about the commit inside the "".
			6.	To link the my github account, I used the following: git remote add origin https://github.com/keefm6776/cookery-website.git
			7.	To push each commit to github I used : git push -u origin master
			8.	For each subsequent commit I repeated steps 3, 4, 5 & 7.

Deployment
I used Heroku to deploy this project by following the steps provided in the CodeInstitute course. To initialise heroku, these were:

			1.	Create an app in heroku, which has an unique name. In my case cookery-website-flask-mongo
			2.	Next login to heroku through the CLI, using the 'heroku login' and entering your heroku credentials.
			3.  To link heroku to the git repository I used the following: 'heroku git:remote -a cookery-website-flask-mongo
			4.	I then sent the command to get it up and running : heroku ps:scale web=1
                After each push to git, step 7, I then used the following command to push to Heroku: git push heroku master

In Heroku, I then set the following Config Variables:

			1.	PORT = 5000
			2	IP   = 0.0.0.0

I was then able to open the app, using this button in Heroku.

Before the final deployment of this project, I have set the debug variable to false in app.py, during the run command for app. 
I have also hidden my MONGO_URI using an environment variable of this name, which is used to set this value for the app.

This project has been deployed via Heroku at :

To run this app locally you need to use the following command in Gitpod, or your IDE's equivelent : python3 manage.py runserver

Testing
Each new feature had been tested after each stage of development within the GITPOD environment. This has included:

After deployment the site has been tested for the above on:

			1.	iPhone 5s on portrait screen (iOS 11 - Safari).
			2.	iPhone 5s on landscape screen. (iOS 11 - Safari)
			3.	iPad Air 2 on portrait screen. (iOS 11 - Safari)
			4.	iPad Air 2 on landscape screen. (iOS 11 - Safari)
			5.  Samsung Galaxy s9 on portrait screen. (Android 8.0.0 (Oreo) - Samsung Internet)
			6.  Samsung Galaxy s9 on landscape screen. (Android 8.0.0 - (Oreo) - Samsung Internet)
			7. 	Hanns-G 20" widescreen monitor. (Windows 10 - Google Chrome 74.0.3729.108, Firefox 66.0.3, MS Edge 42.17134.1.0, Opera 60.0.3255.56)

I have covered all the main browsers on the most common platforms with this testing. I have found that they were all responsive to orientation when applicable, and the site ran as expected in all these scenarios. However, I did find that the manage lists option was missing on a tablet in landscape mode, obviously too big to have the mobile menu and too small to include this option (More Below). I was unable to test Internet Explorer because it would not run on my Windows 10 computer, but I am not particularly concerned as this has a very low market share from between 3-4% from the stats quoted on Wikipedia. At this stage this share would only be decreasing with desktop computers being on the decline and Windows 10 taking over this market with MS Edge.

Resolved Issues:

Code Validation:

#Credits

##Content
			- Before starting this project I looked at various sites recipe based sites, to get a flavour of what is required, these included:
				1.
				2.
				3.
				4.

			- I obtained the sample artefacts for my site from https://https://en.wikipedia.org/wiki/

##Acknowledgements
            - Code institute notes for basics on e-Commerce Website to adapt and base my code on.
              (including Stripe functionality, creation and use of a shopping cart.)
            - Code institute notes for basics on Javascript and JQuery to adapt and base my code on.
            - https://www.w3schools.com/ for information and examples to adapt and base my code on.
            - https://stackoverflow.com/ for information and examples to adapt and base my code on.
            - https://https://en.wikipedia.org/wiki/ for sample artefacts to include in my site.
            - My Mentor Theo Despoudis - for his general guidance.
            - The CI Tutor Team for their repeated help with issues along the way.


