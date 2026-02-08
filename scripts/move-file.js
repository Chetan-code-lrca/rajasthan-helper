const fs = require('fs');
const path = require('path');

const src = 'C:\\Users\\cheta\\rajasthan-helper\\copilot-instructions.md';
const dest = 'C:\\Users\\cheta\\rajasthan-helper\\.github\\copilot-instructions.md';
const dir = 'C:\\Users\\cheta\\rajasthan-helper\\.github';

try {
  // Create .github directory if it doesn't exist
  if(!fs.existsSync(dir)) {
    fs.mkdirSync(dir, {recursive: true});
  }
  
  // Copy the file
  fs.copyFileSync(src, dest);
  
  // Delete the original
  fs.unlinkSync(src);
  
  console.log('File moved successfully');
  console.log('Destination:', dest);
  console.log('Exists:', fs.existsSync(dest));
} catch(err) {
  console.error('Error:', err.message);
  process.exit(1);
}
