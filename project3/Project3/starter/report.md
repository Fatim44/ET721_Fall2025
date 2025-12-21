Student’s Name: Fatima Nadeem  
Professor’s Name: Prof. H  
Class Number: ET 721  
Date: December 21, 2025  

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

Before adding unit tests to the Flask application, the project had very limited test coverage. Most of the application logic and database interactions were not tested at all. Because of this, it was hard to feel confident when making changes to the code. Even small updates could introduce bugs without being noticed right away. At this stage, understanding how different parts of the application worked required manually running the app and checking behavior by trial and error.

After implementing unit tests using pytest, the situation improved significantly. Writing tests for the data models helped confirm that required fields were enforced correctly and that objects were being created as expected. The tests made it easier to verify functionality without manually running the application each time. Overall, the project reached a much more reliable state, with stronger confidence that core features were working properly. Multiple unit tests were added, and test coverage increased to a level appropriate for a real-world application.

## Untested Code: Effects

Working with untested code was difficult and time-consuming. Without tests, it was not always clear how different features were supposed to behave or what edge cases needed to be handled. Errors such as missing required database fields only appeared at runtime, which made debugging more frustrating.

Manually testing the API also required extra steps, such as starting the server, sending requests, and checking responses. This process was slow and made it easy to miss potential problems. These challenges clearly showed why relying only on manual testing is not practical for larger or growing applications.

## Benefits of Unit and API Testing

Unit and API testing provided many benefits to the development process. Unit tests ensured that individual components, such as database models, behaved correctly on their own. API tests helped confirm that endpoints responded properly and handled data as expected. Together, these tests made the application more stable and easier to maintain.

Another major benefit was clarity. The tests acted as documentation, showing how different parts of the application were intended to work. This made it easier to understand the code and would make future updates or collaboration much smoother.

## Role of Continuous Integration (CI)

Continuous Integration (CI) plays an important role in maintaining software quality. By automatically running tests whenever code is pushed to GitHub, CI helps catch errors early. This prevents broken code from being merged and reduces the risk of deployment issues. CI also encourages consistent testing practices and helps maintain long-term project stability.

## Future Improvements

In the future, more tests could be added to cover additional API endpoints and edge cases. Increasing code coverage further and integrating coverage reports directly into the CI workflow would improve visibility into test quality. Adding integration and performance tests would also help ensure the application continues to perform well as it grows.
