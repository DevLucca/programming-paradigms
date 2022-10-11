var fs = require('fs')

function readData(fileName) {
  var data = fs.readFileSync(fileName, 'utf-8')
  return data.split('\n')
}

function resolveSalary(fileData) {
  for (var i = 1; i < fileData.length; i++) {
    var content = fileData[i].split(';')
    
    content[3] = calculateNetSalary(Number(content[1]), Number(content[2]))

    var updatedContent = content.join(';')
    fileData[i] = updatedContent
  }
  return fileData
}

function calculateNetSalary(baseSalary, taxesPercentage) {
  decimalTaxesPercentage = ((100 - taxesPercentage) / 100)
  return baseSalary * decimalTaxesPercentage
}

function saveFile(fileName, fileData) {
  dataJoined = fileData.join("\n")
  fs.writeFileSync(fileName, dataJoined)
}

module.exports = () => {
  fileName = 'dados.csv'
  data = readData(fileName)
  saveFile(fileName, resolveSalary(data))
}
