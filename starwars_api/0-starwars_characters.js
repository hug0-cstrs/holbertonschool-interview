#!/usr/bin/node

const args = process.argv.slice(2); // get arguments from command line input
const URL = 'https://swapi-api.hbtn.io/api/films/' + args[0];
const request = require('request');

const getCharacterName = (link) => { // get character name from link
  const characterName = new Promise((resolve, reject) => { // create promise to return character name
    request(link, (error, response, body) => { // request character name from link
      if (error) console.error('error:', error); // print error if request fails
      resolve(JSON.parse(body).name); // return character name in JSON format
    });
  });
  return characterName;
};

request(URL, async (error, response, body) => { // request characters from URL and print character names
  if (error) console.error('error:', error); // print error if request fails
  const characters = JSON.parse(body).characters; // get characters from URL body response and parse to JSON format
  for (let i = 0; i < characters.length; i++) { // loop through characters and print character names
    const characterName = await getCharacterName(characters[i]); // get character name from link
    console.log(characterName); // print character name
  }
});
