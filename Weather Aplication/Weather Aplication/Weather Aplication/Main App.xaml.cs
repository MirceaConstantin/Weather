using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Timers;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace Weather_Aplication
{
    /// <summary>
    /// Interaction logic for Main_App.xaml
    /// </summary>
    public partial class Main_App : Page
    {

        public string[] lines;

        public Main_App()
        {
            lines = System.IO.File.ReadAllLines(@"./Get_Data_For_App.txt");
            InitializeComponent();
            startclock();
            Current_Day();
            Current_Day_Temp_Image();
            Day_1();
            Day_2();
            Day_3();
            Day_4();
        }

        

        //pozitive incepe de la 0 pana la 49   !!!
       // public string[] pozitive_temp = System.IO.File.ReadAllLines(@"G:\Weather Aplication\Weather Aplication\Pozitive temperature files paths.txt");
        
        //negative incepe de la -1 pana la -30 !!!
        //public string[] negative_temp = System.IO.File.ReadAllLines(@"G:\Weather Aplication\Weather Aplication\Negative temperature files paths.txt");

       //public string abc = @"\Pictures\Temperaturi\temp33.pn";

        private void startclock()
        {
            DispatcherTimer timer;
            timer = new DispatcherTimer();
            timer.Interval = TimeSpan.FromSeconds(1);
            timer.Tick += tickevent1;
            timer.Start();
        }

        private void tickevent1(object sender, EventArgs e)
        {
            Current_Time.Content = DateTime.Now.ToString("HH:mm:ss");
        }


        public void Current_Day()
        {
            string currentday = lines[0].Trim(new Char[] { '(', '\'',')' });
            Current_Date.Content = currentday.Replace("\'", "");
            string Current_Temp = lines[2];
            Current_Humidity.Content= lines[4] + " %";
            Current_Wind.Content = lines[5];
            Current_Wind_Speed.Content = lines[6] + " km/h";
            Current_Status.Content = lines[1];
            string status = lines[1];
            //Current_Temp_Max.Content= lines[3].Remove(5,10);
            //Current_Temp_Min.Content=lines[3].Remove(0,9);

            DateTime now = DateTime.Now;
            DateTime Night = DateTime.Today.AddHours(20.0);

            if (now > Night)
            {
                if (status == "mostly clear")
                    Current_Day_Image.Source = (BitmapImage)Resources["clear_night"];
                if (status == "partly cloudy")
                    Current_Day_Image.Source = (BitmapImage)Resources["fair_night"];
                if (status == "prevailingly cloudy")
                    Current_Day_Image.Source = (BitmapImage)Resources["fair_night"];

            }

            else
            {

                if (status == "mostly clear")
                    Current_Day_Image.Source = (BitmapImage)Resources["clear_day"];
                if (status == "partly cloudy")
                    Current_Day_Image.Source = (BitmapImage)Resources["partly_cloudy_day"];
                if (status == "prevailingly cloudy")
                    Current_Day_Image.Source = (BitmapImage)Resources["fair_day"];

            }

        }

        public void Day_1()
        {
            string day_1 = lines[7].Trim(new Char[] { '(', '\'', ')' });
            Next_day_1.Content = day_1.Replace("\'", "");
            string status = lines[8];
            string Day1_Max_Min = lines[10];
            //string Day1_Max = Day1_Max_Min.Remove(6, 14);
            //string Day1_Min = Day1_Max_Min.Remove(0, 9);

            if (status == "mostly clear")
                Next_day_1_Image.Source = (BitmapImage)Resources["clear_day"];
            if (status == "partly cloudy")
                Next_day_1_Image.Source = (BitmapImage)Resources["partly_cloudy_day"];
            if (status == "prevailingly cloudy")
                Next_day_1_Image.Source = (BitmapImage)Resources["fair_day"];


        }

        public void Day_2()
        {
            string day_2 = lines[14].Trim(new Char[] { '(', '\'', ')' });
            Next_day_2.Content = day_2.Replace("\'", "");
            string status = lines[15];
            string Day2_Max_Min = lines[17];

            if (status == "mostly clear")
                Next_day_2_Image.Source = (BitmapImage)Resources["clear_day"];
            if (status == "partly cloudy")
                Next_day_2_Image.Source = (BitmapImage)Resources["partly_cloudy_day"];
            if (status == "prevailingly cloudy")
                Next_day_2_Image.Source = (BitmapImage)Resources["fair_day"];


        }

        public void Day_3()
        {
            string day_3 = lines[21].Trim(new Char[] { '(', '\'', ')' });
            Next_day_3.Content = day_3.Replace("\'", "");
            string status = lines[22];
            string Day3_Max_Min = lines[24];

            if (status == "mostly clear")
                Next_day_3_Image.Source = (BitmapImage)Resources["clear_day"];
            if (status == "partly cloudy")
                Next_day_3_Image.Source = (BitmapImage)Resources["partly_cloudy_day"];
            if (status == "prevailingly cloudy")
                Next_day_3_Image.Source = (BitmapImage)Resources["fair_day"];


        }

        public void Day_4()
        {
            string day_4 = lines[28].Trim(new Char[] { '(', '\'', ')' });
            Next_day_4.Content = day_4.Replace("\'", "");
            string status = lines[29];
            string Day4_Max_Min = lines[31];

            if (status == "mostly clear")
                Next_day_4_Image.Source = (BitmapImage)Resources["clear_day"];
            if (status == "partly cloudy")
                Next_day_4_Image.Source = (BitmapImage)Resources["partly_cloudy_day"];
            if (status == "prevailingly cloudy")
                Next_day_4_Image.Source = (BitmapImage)Resources["fair_day"];


        }

        public void Current_Day_Temp_Image()
        {
            //pozitive incepe de la 0 pana la 49   !!!
            //string[] pozitive_temp = System.IO.File.ReadAllLines(@"G:\Weather Aplication\Weather Aplication\Pozitive temperature files paths.txt");

            //negative incepe de la -1 pana la -30 !!!
            //string[] negative_temp = System.IO.File.ReadAllLines(@"G:\Weather Aplication\Weather Aplication\Negative temperature files paths.txt");

            string Current_Temp = lines[2];
            int temperature =  Int32.Parse(Current_Temp);
            if (temperature >= 0)
            {
                temperature++;
                string aux = "temp" + Current_Temp;
                Current_Temp_Image.Source = (BitmapImage)Resources[aux]; 
            }

            if (temperature < 0)
            {
                string aux = "temp_" + Current_Temp;
                Current_Temp_Image.Source = (BitmapImage)Resources[aux];
            }
        }
    }
}