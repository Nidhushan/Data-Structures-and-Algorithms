public class Solution {
    public bool IsPalindrome(string s) {
        string sanitizedStr = Regex.Replace(s, "[^a-zA-Z0-9]", "").ToLower();
        string revstr = new string(sanitizedStr.Reverse().ToArray());
        bool isEqual = string.Equals(sanitizedStr, revstr);
        return isEqual;
    }
}

