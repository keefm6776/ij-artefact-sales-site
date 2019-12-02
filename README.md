#MODULE 9 (Full Stack Frameworks With Django) PROJECT - Code Institute Full Stack Developer Diploma
#E-Commerce Website (Artefact Sales)

[![Build Status](https://www.travis-ci.org/keefm6776/ij-artefact-sales-site.svg?branch=master)](https://www.travis-ci.org/keefm6776/ij-artefact-sales-site)

##Project purpose:

In this project, you'll build a full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a artefact/service.

Value provided: By authenticating on the site and paying for some of its services, users can advance their own goals. Before authenticating, the site makes it clear how those goals would be furthered by the site.

The site owner is able to make money by providing this set of services to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.

##BRIEF (CHOSEN PROJECT)

Build an auction place to sell historical artifacts, with the following goals:

1.  External user’s goal:   Find, learn about and acquire artefacts they are interested in

2.  Site owner's goal:      Earn money on selling the artifacts (the site owner is the seller)
    Potential features to include:

    i.  Create an online store focused on selling unique historical artefacts,
        such as The Holy Grail to the highest bidder.

    ii. Allow users to search for artefacts based on various fields.

3.  Allow users to see the price, image and other basic details about an artefact.

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
5.  As the site's owner I want to be able to accept a bid that I deem acceptable for the item.

##Database Design

Before starting this project, I researched various e-commerce websites that are on the web, as mentioned in Credits -> Content, Below. I then set about drawing up a database schema for a relational database as per the project requirements.

##UX

As part of the development process I mocked up wireframes of my recipe site before starting:

See my repository's file list:

.PDF .PDF

Which are located in the Wireframe directory.

##Features

Authentification:

    1)  Any User Must Register and Create a Customer Profile to be able to use the site.
            
    2)  This Customer Profile is used to prepopulate the checkout information, to help make 
        the process easier for the User, all they have to do then is to provide payment details.
        If they wish to have the item delivered to someone else, then they must provide these
        details here.  Due to the value of these artefacts, they must be delivered to the billing
        address used for payment.

    Buyer (Once Logged In):

    3)  The buyer is presented with the artefacts that are currently for sale, newest first, so that 
        he/she can view an image of the artefact, read up on its history and read any other description
        that the seller has provided.
            
    4)  There is a search bar to be able to filter the artefacts by:
    
        i)  Name
       ii)  A range of centuries
      iii)  The era of the item (ie BC or AD)
            
    5)  On each artefact panel there is:
        i) The option to add the artefact to the cart.
       ii) Read more, which presents the history and description of the item to the user.
      iii) Go to the bidding page for this item.

    6)  A link to the cart: 
            
    6)a) Once in the cart:
        i) They can view the items that they have added to the cart.
       ii) For Each Item they can set the required number back to zero, removing it from the cart.
      iii) They can still re-read the history/description of the item.
       iv) They can choose to checkout their selected artefacts.

    6)b) Once having chosen the checkout:
        i) They can check their contact/billing details are correct, or recitfy them
       ii) Provide the card number that they wish to pay with, but it must be the billing address
           of the card, as the details entered are sent to Stripe.
      iii) On having paid for the artefact(s), they are returned to the list of artefacts that are
           still for sale.  (The ones that have just been bought are marked as sold)

    7)  A link to the logged in customer's profile:
        i)  This allows the User to adjust their customer contact details that are used to pre-
            prepopulate the checkout details.

    8)  The Link to Log out:
        i)  This allows the user to log out of their user area.
            
    Seller (Once Logged In):
    
    9)  Along the top menu the seller is able to filter the artefacts as to their current status:
        
        i)  For Sale, the seller (as default) is presented with the artefacts that are currently for sale, 
            newest first, so that he/she can manipulate this data:

            a) The seller can read the information that he/she has provided for the artefact.  
            b) The seller can edit the information that he/she has provided for the artefact.  
            c) The seller can delete the artefact from the database
            
        ii) Sold, the seller is presented with the artefacts that are sold, newest first, however they are
            now unable to edit and delete the information about the artefact:

            a) The seller can search these sold items as per feature 4.
            b) The Seller can still read the information that they have provided for the artefact.
            c) The seller can click the despatch button, this will provide them with a pdf of a 
               despatch note and make the artefact as despatched.


      iii)  Despatched, the seller is presented with the artefacts that are despatched, newest first, however they are
            now unable to edit and delete the information about the artefact:

            a) The seller can search these despatched items as per feature 4.
            b) The Seller can still read the information that they have provided for the artefact.

      NB.  Each of the above three operations are only available while the artefact is still for sale.

    10)     Also on the top menu is add, this when clicked presents the seller with a form that enables
            them to create a new artefact and all the information that can be provided.

    11)     The seller can edit their own profile with the link provided to the right of the top navbar.

    12)     The seller can logout with the link provided to the right of the navbar.



##Features Left To Implement

            1.  Bid Acceptance  -   I have the functionality of a bid process for each artefact so that 
                                    the user can bid on each one (once logged in), or buy the artefact at 
                                    the advertised price.  It still remains to implement a feature for a 
                                    staff user to be able to accept a bid from a given user, and remove
                                    the item from sale, instead of that user paying full price.
##Technologies Used

			1.	GITPOD	        -   All the HTML/CSS/JAVASCRIPT/PYTHON was edited using GITPOD.

			2.	HTML 5 		    -   The structure of the page has been created in HTML5.

			3.	CSS 3	        -   The pages were styled using SS3.

			4.	FONT AWESOME    -   Font Awesome was used to provide the icons throughout the project, as required.

			5.  JAVASCRIPT      -   Javascript used to provide an exit button on various forms where I found it
                                    frustrating not to have one.  Javascript also provided the functionality of
                                    stripe payments which are run using it.

            6.  DJANGO          -   Django was used to provide:
                                        i) The security and feature of logging in and logging out from the site.  
                                       ii) Django has allowed me to allocate users different status depending on 
                                           who they are. i.e.
                                           a)   Superuser - I am the superuser who can access the admin panel and 
                                                            has access to the backend.
                                           b)   Staff     - This is the site owner, who is granted functionality
                                                            related to listing and selling items.
                                           c)   User      - This is the default level, which all customers are given    
                                                            They are only able to see, buy or bid the artefacts and
                                                            are not able to upload artefacts or make changes to them.

                                      iii) The admin panel which allowed me to view and edit models etc.  
                                       iv) Testing suite to be able to run test on the forms, views and models to 
                                           endhance the manual testing that I would have completed whilst developing

			7.	BOOTSTRAP       -	I used Bootstrap to enhance the base HTML for my site, this allowed me to have 
                                    power extras when devloping.  I was provided with:
                                        
                                        i) Navbar and responsiveness between large and small devices.
                                       ii) The pagination for listing pages.  
                                      iii) The grid feature for responsiveness between screen sizes.
                                       iv) Positional commands to allow easy centering of divs and menus, as well
                                           as being able to position them to the left and right.

			8. POSTGRES         -   Postgres (via Heroku) as the relational databse to keep all the information required for this
									project to run and provide all the functionailty of an SQL database.
            
            9. SQL LITE 3		-	SQL Lite 3 was a backup SQL database that would be used in the event of POSTGRES
                                    not being available.  This became invaluable to me while testing with Django,
                                    because I was unable to connect to postgres at that time.

			10.  GOOGLE CHROME DEVELOPER TOOLS
                                -   Used To Test While Developing, checking output and values during processing.
									Testing Functions during development, general tesing of website responsiveness

			11. GIT/GITHUB		-	Used for version control with regular commits.

			12. HEROKU          -   Used to deploy the project.

            13. TRAVIS CI       -   Travis Continuous Integration (CI) testing.  This maintained standards by running 
                                    tests every time I pushed a new commit and reported the results to a pull request.
            
            14. AWS S3 Bucket   -   This allowed me to store my static files in the cloud so that they were available   
                                    to my site at all times.
            
            15. weasyprint (HTML) - Enabled me to create the pdf file which was used as a despatch note for the artefact.

##Git Commits
I have made regular Git Commits during my project for version control and also to allow myself to go back if anything went wrong. I have pushed each of these commits to GitHub, so that the progress of my project can be reviewed. I folowed the steps provided by the GitHub site, which were:

			1.	I set up a page in GITPOD
			
            2.	In the terminal I typed "git init", to initialise the repository
			
            3.	To add files to be committed, I typed "git add ."
			
            4.  To check that these files were staged, I typed "git status" 
                (staged files should be in green font)
			
            5.	To commit these to git, the command "git commit -m "messsage"", was used.  
                With a meaningful message about the commit inside the "".
			
            6.	To link the my github account, I used the following: git remote add origin 
                https://github.com/keefm6776/ij-artefact-sales-site.git
			
            7.	To push each commit to github I used : git push -u origin master
			
            8.	For each subsequent commit I repeated steps 3, 4, 5 & 7.

##Deployment

I used Heroku to deploy this project by following the steps provided in the CodeInstitute course. 
To initialise heroku, these were:

			1.	Create an app in heroku, which has an unique name. In my case ijones-artefact-sales
			
            2.	Next login to heroku through the CLI, using the 'heroku login' and entering your heroku 
                credentials.
			
            3.  To link heroku to the git repository I used the following: 
                'heroku git:remote -a ijones-artefact-sales
			
            4.	I then sent the command to get it up and running : heroku ps:scale web=1
            
            For this project

In Heroku, I then set the following Config Variables:

			1.	PORT = 5000
			2	IP   = 0.0.0.0

Along with:

            3.  STRIPE_PUBLISHABLE Key
            4.  STRIPE_SECRET Key
            5.  DATABASE_URL for postgres
            6.  SECRET_KEY
            7.  AWS_ACCESS_KEY_ID       -   For S3 Bucket
            8.  AWS_SECRET_ACCESS_KEY   -   For S3 Bucket
            
I have also a local copy of these in a file called env.py, which is not being committed to Git/Github that
allows me to run my project locally.

I was then able to open the app, using the Open App button in Heroku.

Before the final deployment of this project, I have set the debug variable to false in settings.py.

This project has been deployed via Heroku at :

                https://ijones-artefact-sales.herokuapp.com/

##Testing
Each new feature had been tested after each stage of development within the GITPOD environment. 

This has included:

Manual Testing:

I have used the site completing each path that can be followed by a user throught the cart and 
checkout and I have also manually tested each link on the site.

Automated Testing:

Using the Django testing suite I have:

    1)  Tested the forms in each app, where applicable, to make sure that the form is not valid
        if is has incomplete data.  I did this by testing each required field to make sure that this
        was the case. See test_forms.py in each app, where applicable.
    
    2)  Tested the models in each app, where applicable, to make sure that the model information is the
        same after being passed throuogh.  I did this by testing each field to make sure that information
        from the model was the same when accessing it with the test_delivery_full_name.delivery_full_name
        format.

        NB.  I was unable to complete these tests when the was an id or an instance involved.  However in
             addition to any automated testing I have also checked these links etc manually.  So these 
             instances where I have been unable to test automatically I have already done so manually.
    
    3)  Tested the views in each app, to make sure that the form is not valid
        if is has incomplete data.  I did this by testing each required field to make sure that this
        was the case. See test_forms.py in each app, where applicable.
    

After deployment the site has been tested for the above on:

	1.	iPhone 7s on portrait screen (iOS 12 - Safari).
	
    2.	iPhone 7s on landscape screen. (iOS 12 - Safari)
	
    3.	iPad Air 2 on portrait screen. (iOS 12 - Safari)
	
    
    4.	iPad Air 2 on landscape screen. (iOS 12 - Safari)
	
    5.  Samsung Galaxy s9 on portrait screen. (Android 8.0.0 (Oreo) - Samsung Internet)
	
    6.  Samsung Galaxy s9 on landscape screen. (Android 8.0.0 - (Oreo) - Samsung Internet)
	
    7. 	Hanns-G 20" widescreen monitor. 
    
    (Windows 10 - Google Chrome 74.0.3729.108, Firefox 66.0.3, MS Edge 42.17134.1.0, Opera 60.0.3255.56)

I have covered all the main browsers on the most common platforms with this testing. 
I have found that they were all responsive to orientation when applicable, and the 
site ran as expected in all these scenarios. 

I was unable to test Internet Explorer because it would not run on my Windows 10 computer, 
but I am not particularly concerned as this has a very low market share from between 3-4% from 
the stats quoted on Wikipedia. At this stage this share would only be decreasing with desktop 
computers being on the decline and Windows 10 taking over this market with MS Edge.



##Resolved Issues:

    Travis CI testing:

        1)  I managed to rectify any early setting errors with the use of Travis.  After this the only
            error was a repeated one, where I had forgotten to comment out the "import env" statement.
    
    Manual Testing:

        1)  I found no padding on the response banner, meaning that it was on top of the register and 
            log in buttons.  Also around the writing that "Indy is retiring", required padding.

        2)  I found that in the Staff log in, when filtering artefact for sale, sold and despatched there
            was no title to confirm this was the filter that was applied for the user. I have now added able
            title in to indicate which filter is being used.

        3)  I found that the highest bid dislayed in the Bids page, was not specific to the artefact that 
            you had clicked to bid on.  In fact I had returned to highest bid in the database.  I then 
            filtered the artefacts with the artefact id that was given by clicking on the artefact that 
            the user wished to bid on.  Furthermore I managed to filter the current customer so only their 
            highest bid for the artefact was displayed, I then realise this error and removed the customer 
            id filter.

        4)  I found that Artefacts were not ordered, potentially giving inconsistent results/ordering when
            displaying artefact records.  This was flagged by the use of pagination on the listing of the 
            artefacts, so I added .order_by('-id') so that it would order the artefacts so that the newest
            id would be shown first.
        
        5)  On testing my checkout view, I found out that when I linked the order to the customer object, I 
            declared it as customer, which had already been used in the stripe code.  I then change my customer 
            object to customer_object.

        6)  On small screens the hidden menu was not listing the items in the menu, however this is now
            rectified.

        7)  On small screens the search banner was too big, so I have re-ordered the fields in it and changed 
            CSS to make it more suitable.

        8)  Also on small screens flexbox made the width of the display container for each artefact too narrow
            so I added a mixin, to make this wider on the smallest screens.
        
        9)  On the profile page, the "You are logged in as:" line was too big, mainly on smaller screens, 
            I have changed this to a more appropriate size.  Also the fields were not centred, so I have 
            used bootstrap to achieve this.

        10)  I found that when there was no image reference in the database that as you would expect, there was 
            no image shown when the artefact was listed.  When this occurs I have displayed a default image, 
            so that there is an image displyed to match the other listings.
         
       11)  Payments - I have tested my payments with Stripe using the following details:

            Card No:        4242 4242 4242 4242
            CCV:            123                     (any three digits)
            Expiry Date:    01/2020                 (any date in the future)
    
    Automated Testing:
    
        1)  Testing with the django test suite I found that a customer information could be added even if
            it was blank.  I have added the 'blank=False' clause to prevent this from happening again, so the
            test would pass. 
        
        

##Unresolved Issues:

    Manual Testing:

        1)  Any artefact can be added via the admin panel or by a staff user via the app.  However when
            using the app I had to remove the image field from the addition because this was causing an 
            error and was not uploading the image.  I have had assitance from a few tutors and was unable 
            to find why this did not upload the file to my S3 bucket, especially considering it worked 
            correctly from the admin panel.  This has meant that I have added the default site image to 
            add as the image for any artefact that has been added via the app that has not image.


##Examination

    For the purpose of examination I have created the following user, which had staff status and
    allows the examier to see the sellers area, allowing the functionality mention above:

    Username :  examiner
    Password :  #letmecheck

    Naturally, you can register yourself as a User to check the selling end of the site.

##Code Validation:



##Content
			- Before starting this project I looked at various selling based sites, to get a flavour 
              of what is required, these included:
				1. Ebay
				2. Amazon
				3. littlewoodsireland.ie
				4. argos.ie

			- I obtained the sample artefacts for my site from https://https://en.wikipedia.org/wiki/

##Acknowledgements
            - Code institute notes for basics on e-Commerce Website to adapt and base my code on.
              (including Stripe functionality, creation and use of a shopping cart.)
            - Code institute notes for basics on Javascript and JQuery to adapt and base my code on.
            - https://www.w3schools.com/ for information and examples to adapt and base my code on.
            - https://stackoverflow.com/ for information and examples to adapt and base my code on.
            - https://simpleisbetterthatcomplex.com/ for information and examples to base my code on.
            - https://https://en.wikipedia.org/wiki/ for sample artefacts to include in my site.
            - My Mentor Theo Despoudis - for his general guidance.
            - The CI Tutor Team for their repeated help with issues along the way.