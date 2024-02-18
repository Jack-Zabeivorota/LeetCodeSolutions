using System;
using System.Collections.Generic;

namespace Testing
{
    public class Solution5
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

    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Result: " + Solution5.LongestPalindrome("baabcedecfg"));
            Console.Read();
        }
    }
}
