using System;
using System.Collections.Generic;

namespace Testing
{
    public class Solution8
    {
        /// <summary>
        /// Повертає перше входження числа в рядку `source`. Якщо число відсутнє, то повертає `-1`.
        /// <code> MyAtoi("  -005864abcd") -> -5864; </code>
        /// </summary>
        public static int MyAtoi(string source)
        {
            List<char> chars = new List<char>();
            bool digitIsFind = false, singIsFind = false;

            for (int i = 0; i < source.Length; i++)
            {
                if (!digitIsFind && !singIsFind && source[i] == ' ') continue;
                else if (!digitIsFind && !singIsFind && (source[i] == '-' || source[i] == '+'))
                {
                    chars.Add(source[i]);
                    singIsFind = true;
                }
                else if (source[i] > 47 && source[i] < 58)
                {
                    chars.Add(source[i]);
                    digitIsFind = true;
                }
                else break;
            }
            if (!digitIsFind) return 0;

            if (int.TryParse(chars.ToArray(), out int result)) return result;

            return chars[0] == '-' ? int.MinValue : int.MaxValue;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Result: " + Solution8.MyAtoi("   -005864   dfsdfbabad"));
            Console.Read();
        }
    }
}
