const fs = require('fs')

// settings
const inDir = 'data/'
const outDir = 'out/'

const inFile = 'a.txt'
const outFile = 'a.txt'

// load data
// data_files = fs.readdirSync(inDir)
// console.log("Data Files:", data_files)
const content = fs.readFileSync(inDir + inFile, 'ascii').split("\n")

// The first line contains five numbers:
// 	an integer D (1 ≤ D ≤ 10 4) - the duration of the simulation, in seconds,
// 	an integer I (2 ≤ I ≤ 10 5) - the number of intersections (with IDs from 0 to I -1 ),
// 	an integer S (2 ≤ S ≤ 10 5) - the number of streets,
// 	an integer V (1 ≤ V ≤ 10 3) - the number of cars,
// 	an integer F (1 ≤ F ≤ 10 3) - the bonus points for each car that reaches its destination before time D .
const headerContent = content[0].split(" ").map(x => parseInt(x))

const D = headerContent[0]
const I = headerContent[1]
const S = headerContent[2]
const V = headerContent[3]
const F = headerContent[4]

const dataContent = content.slice(1, content.length-1).map(x => x.split(" "))

// The next S lines contain descriptions of streets.
var streets = []
var intersections = {}
for (var i = 0; i < S; i++) {
	// Each line contains:
	// two integers B and E (0 ≤ B < I , 0 ≤ E < I ) - the intersections at the start and the end of the street, respectively,
	// the street name (a string consisting of between 3 and 30 lowercase ASCII characters a -z and the character - ),
	// an integer L (1 ≤ L ≤ D ) - the time it takes a car to get from the beginning to the end of that street.
	const B = parseInt(dataContent[i][0])
	const E = parseInt(dataContent[i][1])
	const name = dataContent[i][2]
	const L = parseInt(dataContent[i][3])
	console.log("S>", B, "=>", E, "L:", L, "-", name)
	streets.push({
		B: B,
		E: E,
		name: name,
		L: L
	})

	if (!(B in intersections)) {
		intersections[B] = {
			in: [],
			out: [
				[name, L]
			],
		}
	} else {
		intersections[B].out.push([name, L])
	}

	if (!(E in intersections)) {
		intersections[E] = {
			in: [
				[name, L]
			],
			out: [],
		}
	} else {
		intersections[E].in.push([name, L])
	}
}

for (iId in intersections) {
	console.log("I>", iId)
	console.log("I> I", intersections[iId].in)
	console.log("I> O", intersections[iId].out)
}

// The next V lines describe the paths of each car. Each line contains:
var paths = []
for (var i = S; i < V+S; i++) {
	// an integer P (2 ≤ P ≤ 10 3) - the number of streets that the car wants to travel
	// followed by P names of the streets:
	// 		The car stas at the end of the first street (i.e. it waits for the green light to move to the ext street) and follows the path until the end of the last street. The path of a car is always valid, i.e. the streets will be connected by intersections.
	const P = parseInt(dataContent[i][0])
	const streets = dataContent[i].slice(1)
	console.log("P>", P, "=", streets)
	paths.push({
		P: P,
		streets: streets
	})
}

// TODO: thos two functions can be improved - with alreadyCalculated[]

function getIngoingStreets(intersection) {
	var result = [];

	for (var i = 0; i < streets.length; i++) {
		if (streets[i].E === intersection) {
			result.push(streets[i])
		}
	}

	return result;
}

function getOutgoingStreets(intersection) {
	var result = [];

	for (var i = 0; i < streets.length; i++) {
		if (streets[i].B === intersection) {
			result.push(streets[i])
		}
	}

	return result;
}

var validPaths = [];
var currentTimestamp = 0;
var maxTimestamp = D;

for (var i = 0; i > paths.length; i++) {
	var path = paths[i]

	validPaths.Push({
		isValid: true,
		currentTime: 0,
		currentStreet: path.streets[0]
	})
}


// got data
console.log(D, I, S, V, F)

// process data
schedules = []

// result sample:
schedules = [
	{
		intersectionId: "intersectionIdSample",
		streetSchedules: [
			{
				name: "asdf",
				time: 1,
			},
			{
				name: "asdf2",
				time: 2,
			}
		]
	}
]


// simulate
var intersectionStates = {}
var carStates = paths.map(x => x.streets[0])
var scheduleState = schedules.slice(0)
for (var tick = 0; tick < D; tick++) {
	for (var i = scheduleState.length - 1; i >= 0; i--) {
		const sched = scheduleState[i]
	}


}

// create out data
outData = schedules.length + "\n"
for (var i = 0; i < schedules.length; i++) {
	const sched = schedules[i];
	outData += sched.intersectionId + "\n"
	outData += sched.streetSchedules.length + "\n"
	for (var y = 0; y < sched.streetSchedules.length; y++) {
		const streetSched = sched.streetSchedules[y]
		outData += streetSched.name + " " + streetSched.time + "\n"
	}
}

// write data
fs.writeFileSync(outDir + outFile, outData)
