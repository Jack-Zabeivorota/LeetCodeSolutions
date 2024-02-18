using System;
using System.Collections.Generic;
using System.Linq;

namespace Testing
{
    public class Solution44
    {
        static int FindPart(string source, int start, string part)
        {
            if (part == "") return start;
            int partIdx = 0;

            for (int i = start; i < source.Length; i++)
            {
                if (part[partIdx] == '?' || part[partIdx] == source[i])
                {
                    if (++partIdx == part.Length) return i - partIdx + 1;
                }
                else
                {
                    i -= partIdx;
                    partIdx = 0;
                }
            }
            return -1;
        }

        static List<string> SplitPattern(string pattern)
        {
            List<string> parts = new List<string>();
            int start = 0;

            for (int i = 0; i < pattern.Length; i++)
            {
                if (pattern[i] == '*')
                {
                    if (start < i) parts.Add(pattern.Substring(start, i - start));
                    start = i + 1;
                }
            }
            if (start < pattern.Length) parts.Add(pattern.Substring(start));
            return parts;
        }

        static bool EqualsWithPattern(string source, string pattern)
        {
            if (source.Length != pattern.Length) return false;

            for (int i = 0; i < source.Length; i++)
                if (pattern[i] != '?' && pattern[i] != source[i]) return false;

            return true;
        }

        static bool PartIsHardEnd(string source, string part)
        {
            if (part.Length > source.Length) return false;

            int delta = source.Length - part.Length;

            for (int i = 0; i < part.Length; i++)
                if (part[i] != '?' && part[i] != source[delta + i]) return false;
            
            return true;
        }
        
        /// <summary>
        /// Знаходить співпадіння паттерну (`pattern`) в рядку `source`.
        /// <code> IsMatch("AvBvvvvCvvvv", "A?B*C?*") == true; </code>
        /// </summary>
        public static bool IsMatch(string source, string pattern)
        {
            if (!pattern.Contains('*')) return EqualsWithPattern(source, pattern);

            List<string> parts = SplitPattern(pattern);
            if (parts.Count == 0) return true;

            bool hardStart = pattern[0] != '*';
            bool hardEnd = pattern.Last() != '*';

            int start = FindPart(source, 0, parts[0]);
            if (start == -1 || (hardStart && start > 0)) return false;
            start += parts[0].Length;

            for (int i = 1; i < parts.Count; i++)
            {
                start = FindPart(source, start, parts[i]);
                if (start == -1) return false;
                start += parts[i].Length;
            }
            if (hardEnd && !PartIsHardEnd(source, parts.Last())) return false;

            return true;
        }
    }
    
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Result: " + Solution44.IsMatch("AvBvvvvCvvvv", "A?B*C?*"));
            Console.Read();
        }
    }
}
