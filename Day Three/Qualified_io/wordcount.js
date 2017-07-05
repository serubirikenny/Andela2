function words(str) {
var wordss = str.replace(/[.]/g, '').split(/\s+/);
var freqMap = {};
wordss.forEach(function(w) {
if (!freqMap[w]) {
freqMap[w] = 0;
}
freqMap[w] += 1;
});

return freqMap;

}


