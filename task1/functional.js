var fs = require('fs')

const fileName = 'dados.csv'

const fileData = fs.readFileSync(fileName, 'utf-8').split('\n')

function resolveSalary() {
  const result = []

    for (var i = 1; i< fileData.length; i++) {
      var content = fileData[i].split(';')
      var baseSalary = Number(content[1])
      var taxesPercentage = Number(content[2])
      content[3] = calculateNetSalary(baseSalary, taxesPercentage)

      var updatedContent = content.join(";")
      result.push(updatedContent)
    }
  
  return result
}


function calculateNetSalary(baseSalary, taxesPercentage) {
    const decimalTaxesPercentage = ((100 - taxesPercentage)/100)
    return baseSalary * decimalTaxesPercentage
}

function saveFile() {
  const dataJoined = resolveSalary().join("\n")
  fs.writeFileSync(fileName, dataJoined)
}

module.exports = () => {
  saveFile()
}

