# Fundamentals of Software Architecture
by Mark Richards & Neal Ford

This book examines:  
• Architecture patterns: The technical basis for many 
architectural decisions  
• Components: Identification, coupling, cohesion, partitioning, 
and granularity   
• Soft skills: Effective team management, meetings, negotiation, 
presentations, and more  
• Modernity: Engineering practices and operational approaches 
that have changed radically in the past few years  
• Architecture as an engineering discipline: Repeatable results, 
metrics, and concrete valuations that add rigor to software 
architecture

## Chapter 1
Page 1

### Introduction
- There's no clear career path for Software Architects
- Martin Fowler whitepaper: https://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf
  - > Architecture is about the important stuff…whatever that is.
- Architecture as a role is constantly changing, the wikipedia overview of Software Arch is out of date. 
- Earlier books about  architecture don’t consider DevOps because it didn’t exist when they were written.

### Defining Software Architecture
- Architecture Decisions
- Arhitecture Characteristics
- Design Principles

### Expectations of an Architect
#### Make Architecture Decisions
Ask whether the  decision is helping to guide teams in making the right choice or whether the decision makes the technical choice for them.

- Guide, dont specify
  - e.g: Guidance: use a reactive-based frontend framework. - Then work with the team to choose between React, Angluar, Vue etc.

#### Continually Analyze the Architecture
- Continuously assess if the architecture is still viable today
- Leads to structural decay if you don't
- Includes making Test and Release environments easy to use
- **Keep the application relevant**

#### Keep Current with Latest Trends

#### Ensure Compliance with Decisions

#### Diverse Exposure and Experience
- Technical breadth
- Learn 10 different caching products, not just 1
  - Be able to compare between the options

#### Have Business Domain Knowledge
- Technical expertise coupled with strong knowledge of the business domain
- Communicate with C-level executives and
business users

#### Possess Interpersonal Skills
- "No matter what they tell you, it’s always a people problem.” - [Gerald Weinberg](https://en.wikiquote.org/wiki/Gerald_Weinberg)
- Leadership skills

#### Understand and Navigate Politics
- Negotiation and navigating office politics


### History: Pets.com and Why We Have Elastic Scale
Pets.com appeared in the early days of the internet, hoping to become the Amazon.com of pet supplies.

They had a compelling mascot, a sock puppet. 

Unfortunately, Pets.com apparently spent all the money on the mascot, not on infrastructure. 

Once orders started pouring in, they weren’t prepared. The website was slow, transactions were lost, deliveries delayed, and so on…pretty much the worst-case scenario. So bad, in fact, that the business closed shortly after its disas trous Christmas rush, selling the only remaining valuable asset (the mascot) to a competitor.

What the company needed was **elastic scale**: the ability to spin up more instances of resources, as needed.

In the early days of the internet, companies had to manage their own infrastructure, and many fell victim to a previously unheard of phenomenon: too much success can kill the business.


### Intersection of Architecture and...

#### Engineering Practices
Software Development lacks many features of mature engineering disciplines (e.g Civil Engineers can predict structural change with accuracy).

One of the Achilles heels of software development is estimation—how much time, how many resources, how much money?

#### Knowns and Unknowns
```
…because as we know, there are known knowns; there are things we know we know.
We also know there are known unknowns; that is to say we know there are some things
we do not know. But there are also unknown unknowns—the ones we don’t know we
don’t know.
—Former United States Secretary of Defense Donald Rumsfeld
```

- Unknown unknowns are the nemesis of software systems. 
- Can start with a list of `known unknowns`: things developers must learn about the domain and technology. 
- Cannot start with `unknown unknowns`: things no one knew about which appear out of nowehere.
- Big "design up front" projects suffer - architects cannot design for `unknown unknowns`.
- An **iterative process** fits the nature of software architecture better.

#### The Path from Extreme Programming to Continuous Delivery
- XP created in 1996
- Pushed testing to the extreme, ensured all code was tested before it enters the code base
- XP included engineering practices such as automation, testing, continuous integration
- Led to the book `Continuous Delivery` - updated version of XP practives - led to the `DevOps movement`

#### Fitness Functions
- `Building Evolutionary Architectures` - book
- `architectural fitness functions`: an objective integrity assessment of some architectural characteristic(s)
- e.g - Architect may identify page load time is important, so you build a test into the CI process of the project to report the status of page load time. 
  - Performance benchmarking is similar.

#### Process
- The way that you build software (process) has little impact on the software architecture (structure).
- Historically they have been thought of as mostly separate.
- Now, Architects are using the faster feedback-loop Agile offers and designs are becoming iterative.
- [Strangler Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html) - A software modernization approach that incrementally replaces a legacy system by building a new system around it and gradually shifting functionality and traffic to the new system until the old one can be retired.
- [Feature Toggles](https://trunkbaseddevelopment.com/feature-flags/) - A development technique that lets teams wrap new or unfinished functionality in conditional switches so the code can be merged and deployed safely to production while controlling at runtime whether that feature is enabled for users.


### Laws of Software Architecture
- Everything in software architecture is a trade-off.
- If an architect thinks they have discovered something that isn’t a trade-off, more likely
they just haven’t identified the trade-off yet.
- Why is more important than how.



## Chapter 2
Page 23