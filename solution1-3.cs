using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Testing
{
    public class Solution1
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
        /// <code> IsMatch("vavbvvvvcvvvv", "?a?b*c?*") == true; </code>
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

    public class Solution2
    {
        struct Range
        {
            public int Start, End;
            public readonly int Delta => End - Start;
            public Range(int start, int end)
            {
                Start = start;
                End = end;
            }
        }

        static char[] GetReverse(List<char> chars)
        {
            char[] reverseChars = new char[chars.Count];
            int i = reverseChars.Length;

            foreach (char c in chars)
                reverseChars[--i] = c;

            return reverseChars;
        }

        static string GetPalindrome(string source, Range range)
        {
            // if (source.Length == 1) return source;
            // if (range.Start < 0 || range.End >= source.Length) return "";

            string centerSequence = new string(source[range.Start], range.Delta + 1);

            int left_idx = range.Start, right_idx = range.End;

            List<char> chars = new List<char>();


            while (--left_idx >= 0 && ++right_idx < source.Length && source[left_idx] == source[right_idx])
                chars.Add(source[right_idx]);

            return $"{string.Join("", GetReverse(chars))}{centerSequence}{string.Join("", chars)}";
        }

        static List<Range> GetRangesOfSequence(string source)
        {
            if (source.Length == 0) throw new Exception("source is empty");
            if (source.Length == 1) return new List<Range> { new Range(0, 0) };

            List<Range> ranges = new List<Range>();
            int start = 0;

            for (int i = 1; i < source.Length; i++)
            {
                if (source[start] != source[i])
                {
                    ranges.Add(new Range(start, i - 1));
                    start = i;
                }
            }
            ranges.Add(new Range(start, source.Length - 1));

            return ranges;
        }

        /// <summary>
        /// Знаходить в рядку `source` найдовший рядок-паліндром та повертає його.
        /// <code> LongestPalindrome("baabcedecfg") -> "cedec"; </code>
        /// </summary>
        public static string LongestPalindrome(string source)
        {
            if (source.Length < 2) return source;

            List<Range> ranges = GetRangesOfSequence(source);

            string maxPalindrome = "";

            foreach (Range range in ranges)
            {
                string palindrome = GetPalindrome(source, range);
                if (palindrome.Length > maxPalindrome.Length)
                    maxPalindrome = palindrome;
            }

            return maxPalindrome;
        }
    }

    public class Solution3
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
            Console.WriteLine("Result: " + Solution3.MyAtoi("   -005864   dfsdfbabad"));
            Console.Read();
        }
    }
}
