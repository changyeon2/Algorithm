SELECT 
    FirstName, LastName, City, State
FROM 
(
    Person
        LEFT JOIN 
    Address ON person.PersonId = Address.PersonId;
)
