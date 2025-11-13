using SpiritValleyArchipelagoClient.Archipelago;
using System;
using System.Security.Cryptography;
using System.Text;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Util
{
    public class Crypt
    {
        public static string Encrypt(string inputString)
        {
            if (string.IsNullOrEmpty(inputString)) { ArchipelagoConsole.LogMessage("ERROR TRYING TO SAVE GAME DATA JSONDATA IS NULL OR EMPTY"); }
            string text;
            using (Aes aes = Aes.Create())
            {
                aes.Key = Encoding.ASCII.GetBytes("MTFFmGj6daEmOmWSp6IhUUznWOXhyHO0");
                aes.IV = Encoding.ASCII.GetBytes("MYWdttm2tKXZRmvJ");
                byte[] bytes = new UnicodeEncoding(false, false, true).GetBytes(inputString);
                text = Convert.ToBase64String(aes.CreateEncryptor(aes.Key, aes.IV).TransformFinalBlock(bytes, 0, bytes.Length));
            }
            return text;
        }

        public static string Decrypt(string inputString)
        {
            string text;
            using (Aes aes = Aes.Create())
            {
                aes.Key = Encoding.ASCII.GetBytes("MTFFmGj6daEmOmWSp6IhUUznWOXhyHO0");
                aes.IV = Encoding.ASCII.GetBytes("MYWdttm2tKXZRmvJ");
                byte[] array = Convert.FromBase64String(inputString);
                byte[] array2 = aes.CreateDecryptor(aes.Key, aes.IV).TransformFinalBlock(array, 0, array.Length);
                text = new UnicodeEncoding(false, false, true).GetString(array2);
            }
            return text;
        }
    }
}
