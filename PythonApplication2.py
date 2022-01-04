using System;

namespace EpicBattle
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] heroes = { "Hog Rider", "Goblin", "Colt", "Spike" };
            string[] villain = { "BlackMan", "NickErr", "Hitler", "Mortis", "Fatman" };




            string randomHero = GetrandomCharacter(heroes);
            string randomVillain = GetrandomCharacter(villain);
            string heroWeapon = GetWeapon();
            string villainWeapon = GetWeapon();
            Console.WriteLine($"{randomHero} with {heroWeapon} will fight {randomVillain} with {villainWeapon});
            Console.WriteLine($"Your random hero is {randomHero}");
            Console.WriteLine($"Your random villain is {randomVillain}");
        }

        public static string GetrandomCharacter(string[] someArray)
        {
            

            return someArray[GetRandomIndexForArray(someArray)];
        }

        public static string GetWeapon()
        {
            string[] weapon = { "Sausage", "Pan", "Ak47", "Pickle", "DickJohnson" };
            return weapon[GetRandomIndexForArray(weapon)];

           
        }

        public static int GetRandomIndexForArray(string[] someArray)
        {
            Random rnd = new Random();
            return rnd.Next(0, someArray.Length);
        }


    }
}
