## Vibe coding notes

This is a sort of journal of my (Andy's) vibe coding experience as some things to be careful of.  

- It's tempting to generate code quickly without truly understanding all that is happening.  you get working code right away!  but this also caused some issue.  Here were some.

- I didn't initially realize that AVATAR, when there was only one patient at a dose level receiving a dose at a certain time, the algortihm wouldn't blend patients, it would just add noise to teh data.  Similarly, if there was only one patient 

- It can should be documented what and how the code was reviewed and at what time.  I wonder if this sort of thing can be automatically done?

- One useful approach is to have it rite documentation, especially high level.  Then read it?  Does ti make sense?  If not, rewrite it, ask questions, maybe even change method or develop new tests.  Once it's gotten kind of stable, then you catually hane to review the code.  Could have a different method do an audit and also suggest the most critical points where you should review. 


thoughts from colleague
- adverserial loop, where one agent reviews and one agent codes
- Devil's advocate agent to build counter arguments against plan or code.
- rubber duck - makes me explain solution to rubber duck.  then test me at it.
- write lots of tests.  4 kinds of testing (unit tests, integration tests, system tests, and acceptance tests)