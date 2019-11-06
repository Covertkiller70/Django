var fname = prompt('Enter First Name: ').toLowerCase();
var lname = prompt('Enter Last Name: ') .toLowerCase();
var age = prompt('Enter age: ').toLowerCase();
var height = prompt('Enter your height: ').toLowerCase();
var petname = prompt('Enter pet name: ').toLowerCase();

if (fname[0] === lname[0] && age <= 30 && age >= 20 && height >= 170 && petname[petname.length -1] === 'y'){
    console.log('welcome mr spy');
}
else{
    console.log('Go away you!');
}