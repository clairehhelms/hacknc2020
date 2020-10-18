# hacknc2020
Repository for HackNC project by Fernando Garcia, Jenn Kang, and Claire Helms

This project is based off of the idea of speed-dating. The idea is to match language students and teachers to engage in enriching, short conversations to aid in learning new languages. 

The problem with other language-learning apps and websites is that one-on-one conversation cannot happen with live speech, and often, conversations get into a rut by repetetive introductions and basic questions.

We definitely want to expand this project to include a profile page and matching criteria based on experience and interests. We also want to create three tracks for users: student, teacher, and combination. These tracks dictate which role you will play in a conversation: native speaker or learner. We would also like to incorporate an incentive-based points system based off of conversation participation. 

We learned so much in this project. Fernando and Claire learned the basics of HTML, running sites locally, and Flask (a Python extension). Jenn learned how to implement open source projects and utilize Youtube videos to aid my understanding of various programming languages and extensions. She learned how to write JavaScript and the JSON data format. We all learned how to work as a team and began to bring our conceptual ideas into tangible reality through programming!

## Inspiration
After reviewing other language applications available in the app store (such as “HelloTalk”), we realized that there are no language websites or apps that incorporate “speed exchange” concept to language. However, after discussing with the team, we came to the conclusion that that may be one of the most effective way to learn a new language: talking to many people with different accents and dialects talking about diverse topics (so that you can practice the language other than simply talking about your age, hobbies, purpose of learning a foregin language etc.). By having a timer, you are automatically assigned to a different language group or partner so that you don’t have to worry about having an awkward talk to exit out of the conversation if the convo is getting too long or going off on a tangent. When you first log in to the app, you can choose which language you want to learn, which language you are fluent in, and which topic you want to talk about. Then starts the timer where you have a short 3-5 minutes to converse with your partner in your target language. Then boom! Partner change! After every exchange, you have the option to “favorite” a partner if you would like to be matched with that person again in the future. Happy language learning!

## What it does
This project allows a user to join a video call with another user in order to have a quick dialogue in a new language. The front-end site is straightforward and leads the user to the second site, where there is a randomly generated prompt/question for the video call. The video call software is not embedded, but once a user gets to the video exchange site, they can talk to another user using a secure browser.

## How we built it
We learned how to use and understand basic HTML to create a front-end local website that covers the UX of entering the website. We included a button to the next website, which we linked by using Flask. Flask checks the local website route, and depending on the route, goes to the correct page. We also used Flask to communicate between the Python file and the HTML files to randomize the question prompted when entering the second website. For a smooth video exchange experience incorporated inside the website, we implemented our own video conferencing platform (instead of using other third-party sources like zoom or skype) where users will receive secure URLS provided only to the language partner or group. This was built using Node.js.

## Challenges we ran into
We realized quite quickly that we did not have enough time nor a large enough technical skillset to complete all of our big ideas, so we had to consolidate our product to the bare bones of our idea. This included ditching the idea of timing the call, matching users to create a personalized UX, and publishing to a real domain. We also ran into difficulty linking the sourced video server to the HTML pages we created, and we ended up not finishing embedding the video. We also ran into some smaller problems linking pages to each other and merging our individual work. We were able to solve all minor and major challenges, though, by good communication and teamwork facilitated by our individual mindsets and our use of github to collaborate. We came to have fun and enjoy the challenge, and we definitely did!

## Accomplishments that we're proud of
In the case of two of our members, Fernando and Claire, it was their first time utilizing HTML and Flask. In the end, they were able to effectively combine their knowledge of Python and HTML, to create a local website, they would not have been able to make before starting the hackathon. Similarly, many of the members were new or inexperienced with Github, and learned to navigate the site throughout their time in the competition. Overall, the group was proud of their efforts, with all members being first time Hackathon participants. Moreover, the effective communication and teamwork they displayed throughout their time working on the project, helped them create a project they could say they put their all into. 

## What we learned
We learned so much in this project. Fernando and Claire learned the basics of HTML, running sites locally, and Flask (a Python extension). Jenn learned how to implement open source projects and utilize Youtube videos to aid my understanding of various programming languages and extensions. She learned how to write JavaScript and the JSON data format. We all learned how to work as a team and began to bring our conceptual ideas into tangible reality through programming!

## What's next for Speed Speed Lang
We definitely want to expand this project to include a profile page and matching criteria based on experience and interests. We also want to create three tracks for users: student, teacher, and combination. These tracks dictate which role you will play in a conversation: native speaker or learner. We would also like to incorporate an incentive-based points system based off of conversation participation.

## link to youtube: 
https://youtu.be/67ZiKZD_u8M

## Video Walkthrough
<img src= "https://recordit.co/gb4NOAiq02.gif" title='Video Walkthrough' width='' alt='Video Walkthrough' />
<img src= "http://g.recordit.co/xsXCnZnhul.gif" title='Video Walkthrough' width='' alt='Video Walkthrough' />


