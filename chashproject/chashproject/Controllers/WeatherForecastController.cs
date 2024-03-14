using Microsoft.AspNetCore.Mvc;
using chashproject.Services;
using System;
using System.Collections.Generic;
using System.Linq;



namespace chashproject.Controllers
{
    [Route("api/[controller]")]
    [ApiController]

    public class EntitiesController : ControllerBase
    {
        private readonly MockDatabaseService _databaseService;

        public EntitiesController(MockDatabaseService databaseService)
        {
            _databaseService = databaseService;
        }

        [HttpGet]
        public IActionResult GetAllEntities([FromQuery] int page = 1, [FromQuery] int pageSize = 10)
        {
            var entities = _databaseService.GetAllEntities();
            var paginatedEntities = entities.Skip((page - 1) * pageSize).Take(pageSize).ToList();
            return Ok(paginatedEntities);
        }

        [HttpGet("{id}")]
        public IActionResult GetEntityById(string id)
        {
            var entity = _databaseService.GetEntityById(id);
            if (entity == null)
                return NotFound();

            return Ok(entity);
        }

        [HttpGet("search")]
        public IActionResult SearchEntities([FromQuery] string search)
        {
            var entities = _databaseService.GetAllEntities().Where(e =>
                e.Names.Any(n => (n.FirstName + " " + n.Surname).Contains(search)) ||
                e.Addresses.Any(a => (a.AddressLine + ", " + a.Country).Contains(search))
            ).ToList();

            return Ok(entities);
        }

        [HttpGet("filter")]
        public IActionResult FilterEntities([FromQuery] string gender, [FromQuery] DateTime? startDate, [FromQuery] DateTime? endDate, [FromQuery] string[] countries)
        {
            var entities = _databaseService.GetAllEntities();

            if (!string.IsNullOrEmpty(gender))
                entities = entities.Where(e => e.Gender == gender).ToList();

            if (startDate != null)
                entities = entities.Where(e => e.Dates.Any(d => d.DateValue >= startDate)).ToList();

            if (endDate != null)
                entities = entities.Where(e => e.Dates.Any(d => d.DateValue <= endDate)).ToList();

            if (countries != null && countries.Length > 0)
                entities = entities.Where(e => e.Addresses.Any(a => countries.Contains(a.Country))).ToList();

            return Ok(entities);
        }
    }
}
