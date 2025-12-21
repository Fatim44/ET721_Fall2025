Student’s Name: Fatima Nadeem  
Professor’s Name: Prof. H 
Class Number: ET 721  
Date: December 21, 2025  

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

Before adding unit tests, the Flask application had very little test coverage. Most features and database interactions were untested, which made it difficult to confidently modify the code. Small changes could easily cause errors that were not immediately noticeable, and much of the testing had to be done manually.

After implementing unit tests with pytest, the project became much more reliable. Tests were added to verify that models were created correctly and that required fields were enforced. This improved confidence in the application and reduced the need for manual testing. Overall, test coverage increased and the code became easier to maintain.

## Untested Code: Effects

Working with untested code made debugging harder and more time-consuming. Errors often appeared only at runtime, and understanding expected behavior required manually running the application. This showed how risky it is to rely only on manual testing.

## Benefits of Unit and API Testing

Unit and API tests helped ensure that individual components and endpoints behaved as expected. The tests also served as a reference for how the application should work, making the code easier to understand and update.

## Role of Continuous Integration (CI)

Continuous Integration helps maintain code quality by automatically running tests when changes are pushed to GitHub. This allows problems to be caught early and prevents broken code from being merged.

## Future Improvements

Future improvements could include adding more tests for edge cases and API endpoints. Increasing coverage and adding integration tests would further improve application stability.
