using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Weather_Aplication
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            Return_but.Visibility = Visibility.Hidden;
            Main.Content = new Main_App();
            Background_Image();
        }
        private void DragBar(object sender, MouseButtonEventArgs e)
        {
            base.DragMove();
        }

        private void Close_button(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }

        private void Minimize_button(object sender, RoutedEventArgs e)
        {
            WindowState = WindowState.Minimized;
        }

        private void Info_button(object sender, RoutedEventArgs e)
        {
            Main.Content = new About();
            Info_but.Visibility = Visibility.Hidden;
            Return_but.Visibility = Visibility.Visible;
        }

        private void Return_button(object sender, RoutedEventArgs e)
        {
            Main.Content = new Main_App();
            Info_but.Visibility = Visibility.Visible;
            Return_but.Visibility = Visibility.Hidden;
        }

        public void Background_Image()
        {
            string[] lines = System.IO.File.ReadAllLines(@"./Get_Data_For_App.txt");
            DateTime now = DateTime.Now;
            //DateTime Day = DateTime.Today.AddHours(9.0);
            DateTime Night = DateTime.Today.AddHours(20.0);

            if (now > Night)
            {
                if (lines[1] == "mostly clear")
                    back_image.ImageSource = (BitmapImage)Resources["clear_n"];
                if (lines[1] == "partly cloudy")
                    back_image.ImageSource = (BitmapImage)Resources["cloudy_n"];
                if (lines[1] == "prevailingly cloudy")
                    back_image.ImageSource = (BitmapImage)Resources["cloudy_n"]; 
            }
            else
            {
                if (lines[1] == "mostly clear")
                    back_image.ImageSource = (BitmapImage)Resources["clear_d"];
                if (lines[1] == "partly cloudy")
                    back_image.ImageSource = (BitmapImage)Resources["cloudy_d"];
                if (lines[1] == "prevailingly cloudy")
                    back_image.ImageSource = (BitmapImage)Resources["cloudy_d"]; 
            }
        }
    }
}



