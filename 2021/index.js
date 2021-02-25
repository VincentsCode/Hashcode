const fs = require('fs')

// settings
const inDir = 'data/'
const outDir = 'out/'

const inFile = 'a.txt'
const outFile = 'a.txt'

// load data
// data_files = fs.readdirSync(inDir)
// console.log("Data Files:", data_files)
console.log("Processing:", inFile)
const data = fs.readFileSync(inDir + inFile, 'utf8')
console.log(data)


// process data



// write data
fs.writeFileSync(outDir + outFile, 'test')
console.log("Written:", outFile)