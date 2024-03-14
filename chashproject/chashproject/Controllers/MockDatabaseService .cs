using System;
using System.Collections.Generic;
using System.Linq;

namespace chashproject.Services
{
    public class MockDatabaseService
    {
        private List<Entity> _entities;

        public MockDatabaseService()
        {
            _entities = new List<Entity>();
            
            _entities.Add(new Entity { Id = "1", Names = new List<Name> { new Name { FirstName = "John", Surname = "Doe" } } });
            _entities.Add(new Entity { Id = "2", Names = new List<Name> { new Name { FirstName = "Jane", Surname = "Smith" } } });
        }

        public List<Entity> GetAllEntities()
        {
            return _entities;
        }

        public Entity GetEntityById(string id)
        {
            return _entities.FirstOrDefault(e => e.Id == id);
        }

        
    }

    
    public class Entity
    {
        public List<Address> Addresses { get; set; }
        public List<Date> Dates { get; set; }
        public bool Deceased { get; set; }
        public string Gender { get; set; }
        public string Id { get; set; }
        public List<Name> Names { get; set; }
    }

    public class Address
    {
        public string AddressLine { get; set; }
        public string City { get; set; }
        public string Country { get; set; }
    }

    public class Date
    {
        public string DateType { get; set; }
        public DateTime DateValue { get; set; }
    }

    public class Name
    {
        public string FirstName { get; set; }
        public string MiddleName { get; set; }
        public string Surname { get; set; }
    }
}
