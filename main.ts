interface Student {
    firstName: string,
    lastName: string,
    age: number,
    location: string,
}
const stud1: Student = {
    firstName: "student",
    lastName: "1",
    age: 19,
    location: "Ethiopia",
}
const stud2: Student = {
    firstName: "student",
    lastName: '2',
    age: 20,
    location: "Eritrea",
}
const studentsList = [stud1, stud2];
var table = document.createElement('table');
document.body.appendChild(table);

studentsList.forEach(function(row) {
  var tr = document.createElement('tr');
  table.appendChild(tr);
  var firstNameElement = document.createElement('td');
  var locationElement = document.createElement('td');
  firstNameElement.innerHTML = row.firstName;
  locationElement.innerHTML = row.location;
  tr.appendChild(firstNameElement);
  tr.appendChild(locationElement);
});
document.body.appendChild(table);