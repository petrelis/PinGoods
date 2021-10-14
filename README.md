# Software Engineering project "PinGoods"
# Group II
PinGoods is a local goods platform dedicated to easily connecting vendors with their customers.

## 1. Purpose

There was once a potato lover who wanted to buy fresh potatoes straight from the farm (because Maxima potatoes are not so tasty). Unfortunately, he didn‘t know anyone who could sell them to him. He looked for them on Facebook, but couldn‘t find a single person. He searched the entire internet but was not able to find a place to contact a potato grower. We could make a new Facebook (but with superior search algorithms of course), but we're too cool for that. Besides, we have an even better idea. On the other side, it‘s not all sunshine and rainbows either. Potato sellers also have a hard time finding someone to buy from them (not because they can‘t navigate Facebook, but because there is no good platform for such things). And that‘s where we come in. We will create a platform that will easily connect not only potato lovers with their sellers, but also various vendors to their customers, and they will all live in great prosperity.

## 2. High-Overview

The aim of the system is to ensure that goods from the villages of all Lithuanian regions can display their purchase location on the map, and when the customer selects the result in the search bar, he gets teleported to the seller's location. What does this really mean? Obviously, we are not making a breakthrough in human evolution (not yet anyway), but rather we are offering the sellers a possibility to advertise their goods, and for the buyers to be informed of desirable existing goods, conveniently pinned on the map. The system will provide the best environment for small businesses to showcase their high-quality products and services. Product prices will be clearly stated including Value-added tax (PVM). Customers will also be able to take advantage of our intuitive sorting system, thanks to a great variety of colours as if van Gogh drew it. All available functions can be seen in the diagram below.

![Use-Case Matrix](https://user-images.githubusercontent.com/47245874/135151107-f3b1b202-6b2b-44f3-bc39-605a59cab5e9.png)

Each user role interaction with our project functionalities:

![Use-Case Diagram](https://user-images.githubusercontent.com/47245874/137365714-11c54df7-1938-449c-8273-8d4b15c6677f.png)

Our deployment diagram containing the physical hardware and software of the system and their interaction:

![Deployment Diagram](https://user-images.githubusercontent.com/47245874/137366413-53f24f3f-feea-4e57-b2e8-3844a2d48e9a.png)

All external entities of our system and their interaction:

![System Contex Diagramt](https://user-images.githubusercontent.com/47245874/137367098-147fdcba-6023-41b7-8ae5-77a21983dddb.png)

Workflow of the activity sequence in our project system, detailing the progression of events from the start to the finish:

![Activity Diagram](https://user-images.githubusercontent.com/47245874/137367706-4f2a6ac6-3c1e-4a22-92b6-9b8a1048bb1c.png)


## 3. The Great Gang

Each project member chose a working team in which is most comfortable. This was done to save time and improve efficiency. As a well-coordinated team, we will collaborate with the rest of the team. We selected these specific teams as a part of our project. Why? Because the big guys on the internet said these specific teams should be enough for any project. And we decided to go for it.

**Lead: Sahak Ivašauskas @sahiva**

- **Front-End**
  - **Gustas Petkevičius @FlooPeriS (Sub-Lead)**
  - Sara Sánchez @SaraSanGar
  - Danielius Miškinis @Segulx
  - Pablo Santana @pablosanttanaa
  - Liudas Kraujalis @Liudaskr
  - David Kisel @DavidK14
  - Maksym Hrynak @hrymasik
  
- **Back-End**
  - **Marius Raupelis @mariusraupel (Sub-Lead)**
  - Martynas Jakučionis @Jaku12345
  - Gustas Strimaitis @Radorkan
  - Aurimas Miliauskas @AuriTheGreat
  - Petras Rudys @petrelis
  - Faustas Baltrušaitis @FaustasYe
  - Yeeun Lee @Atay36
  - Chiara Satta @chiarasatta
  - Arnas Navikas @kozahr

- **Server**
  - **Sahak Ivašauskas @sahiva (Sub-Lead)**
  - Taha Abakar Samir @samir737
  
- **Graphics**
  - David Kisel @DavidK14
  - Martynas Jakučionis @Jaku12345

- **Documentation**
  - Sahak Ivašauskas @sahiva

## 4. Mandatory Functionality

One of the key functionalities that our project will consist:

**4.1. HOMEPAGE** 

This is the page that the user sees once he visits the website. 
- At the top, there is the primary button. Clicking it leads you to the main page, which includes the following functionalities:
  - Search bar 
  - Map 
  - Options Bar 
- Under the button, the description of the website is displayed.

**4.2. REGISTRATION WINDOW**

At the top-right of the home page, there are "Login" and "Registration" fields. Clicking the "Log in" button opens the "Log in" window. In that window, the user will have to enter his username or e-mail address in the "Username or e-mail address" field and the password in the "Password" field. That window will also have a button titled "Log in" and a text box as "If you are not registered, register." where "Register" is the text associated with the registration window. After clicking on the main page "Register" button - you'll see a window where you can register, whether you are registering as a seller or a buyer. If you are registering as a seller, a window will appear with the required fields to fill in: 
- Username
- First/Last name
- Phone number (optional as instead, it'll be next to the product) 
- City of residence 
- Address (optional as instead, it'll be next to the product)
- Password 
- Repeat password

If you register as a customer, a window will appear with a required fields to fill in: 
- Username
- City of residence (optional)
- Password 
- Retype password 

Some other information may be added later on to be filled in. Upon registration, **noreply@pingoods.com** will send a message with confirmation to the user.

**4.3. MAP** 

It is located in the centre of the home page on the right side of the search bar. After submitting a search query to the search bar: 
- In the enlarged window, the user sees all the results that best match the search criteria. 
- When zoomed in, the user sees all the products in the area that match the criteria. 
- Clicking on one of the search results will take you to that seller on the map.

**4.4. SEARCH BAR** 

Clicking the primary button on the homepage leads you to the main page with the Search Bar. It'll be located at the top-left of the page. After the search, the search bar will list the most relevant results for the products, and the goods and services tax (PVM) adjusted prices will be displayed. The most suitable product is determined by the combination of your preferred results (vendor's subscription products will be at top), selected categories (product colour), keyword best match, and closest customer distance.

**4.5. OPTIONS BAR**

If the user has logged in to the system, it's located at the top-right of the Main Page. Otherwise, it's not so. When the registered user clicks the button, it'll display for **Vendors**:
- Subscription. Clicking it will display buttons, allowing to: 
  - Buy subscription
  - Check subscription history 
- Edit product posts. Clicking it will display buttons, allowing to:
  -  Edit location 
  -  Edit price
  -  Delete the post
    - Once the remove button is clicked, a confirmation screen will appear in the centre. 
  - Change Phone Number
  - Change City of Living  
  - Change Address 
  - Change Password

If it's clicked by a **Customer**, then he'll get displayed with:
  - History of Purchases 
  - Change Phone Number 
  - Change City of Living 
  - Change Address 
  - Change Password

## 5. Non-Functional Requirements

We, as a team, are expecting that the following non-functional requirements won't cause stress to our users. The software program will have a clear-as sky (not like what we see every day) interface mixed with bright colours! 

**5.1. SECURITY**

Our login and registration system will be as simple as putting on your pants (although sometimes it can be complicated, especially on Monday mornings). and we will implement these security measures for your comfort:
  - Database will only be accessible to administrators.
  - Email and postal address will not be visible in the profile of the customers.
  - The software will detect the existence of two customers with the same ID. (so that you cannot buy from yourself)
  - Age limit to prevent your kids from spending your savings.

**5.2. OPTIMIZATION**

The website may be so optimized that it may even run on a grandmother's cell phone. We guarantee that:
  - The loading time won't exceed 4 seconds, so you will not get bored surfing our webpage. (because who likes to wait more than 4 seconds?)

## 6. Documentation

   The provided information must be referred by the developers in their workflow to prevent disorder and misunderstandings.

   ### 6.1 GitHub formatting

   GitHub formatting [syntaxes](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) should be known for formatting your issue description and commits.

   ### 6.2 Issues

   Issues are created for setting tasks and reporting bugs. All the Issues title must be as follows: "[**TEAMNAME**-**ISSUEID**] **ISSUENAME**", where **TEAMNAME** is the shortcut of the team that must handle this Issue, **ISSUEID** is a unique identification number for each team's Issue, **ISSUENAME** is the short title for the issue. Use uppercase letters appropriately in the title.

   [How We Write GitHub Issues](https://wiredcraft.com/blog/how-we-write-our-github-issues/)

   **6.3 Shortcuts for each team**

   - **Front-End** - **FRNT**
   - **Back-End** - **BACK**
   - **Server** - **SERV**
   - **Graphics** - **GFX**
   - **Documentation** - **DOCS**

   **6.4 Setting Issue fields**

   - **Assignee**: to solve this Issue, assign a specific developer list. Set to null if the problem is not someone's concern, especially
   - **Label**: select the appropriate label for the Issue, including the label of the team to which it is assigned. **If the Issue is a bug**, then **bug** label must be set as well
   - **Projects**: must be set to the team to which the Issue belongs
   - **Milestone**: set the Issue to an appropriate release


   **6.5 Issue Description**

   **If the Issue is a task**, then write a clear, atomic specification of the task. If needed, use visual content, checkboxes, etc.
   
   **If the Issue is a bug**, then shortly describe the problem and write down what is the **Expected result:** and the **Actual result:**.
   
  ### 6.6 Gitflow Workflow

   This [article](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) contains the git-flow model that should be followed when creating, merging, and deleting branches. For naming branches, please refer to the git branch naming [convention](https://deepsource.io/blog/git-branch-naming-conventions/). **Important!: don't use the tracker ID in the branch name as it's provided in the article. We're not going to use it.**

  ### 6.7 Coding conventions

  Each developer has a different coding style, and to avoid confusion, you should follow the Google Style Guide for each programming language.

  -  [**JavaScript**](https://google.github.io/styleguide/jsguide.html)
  -  [**HTML/CSS**](https://google.github.io/styleguide/jsguide.html)
  -  [**Java**](https://google.github.io/styleguide/javaguide.html)
  -  [**PHP**](https://www.php-fig.org/psr/psr-2/)

  

