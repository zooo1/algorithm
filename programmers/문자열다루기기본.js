function solution(s) {
    if ((s.length === 4 || s.length === 6) && (s == parseInt(s))) return true;    
    return false;
}