public class Solution {
    public bool IsValid(string s) {
        // Console.WriteLine($"{s}");
        Stack<char> stck = new Stack<char>();
        foreach (char ch in s)
        {
            if (ch == '(' || ch == '{' || ch == '[') 
            {
                stck.Push(ch);
            }
            else if (ch == ')' || ch == '}' || ch == ']')
            {
                if (stck.Count() == 0 ||
                    (stck.Peek() != '{' && ch=='}') || 
                    (stck.Peek() != '(' && ch==')') ||
                    (stck.Peek() != '[' && ch==']'))
                    {
                        return false;
                    }
                stck.Pop();
            }
        }
        if (stck.Count() == 0)  
            return true;
        return false;
    }
}

