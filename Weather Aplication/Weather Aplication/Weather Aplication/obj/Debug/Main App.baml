   M S B A M L   `   `   `  ����M  IWeather Aplication, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null7 clr-namespace:Weather_AplicationWeather_Aplication  5      O Kmscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e0891&clr-namespace:System;assembly=mscorlibSystem 5      !    Weather_Aplication.Main_App   5      \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5      Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5      @d2http://schemas.microsoft.com/expression/blend/2008     5      2local clr-namespace:Weather_Aplication     5      6clr&clr-namespace:System;assembly=mscorlib     5        N� Title$  Main_App��5
      $	��518��6   $	��320��6&    N� 
Background 62   Z�  � 	Resources 5         fair_day �� 	UriSource 
 temp20 
 temp21 
 temp24 
 temp30 
 temp40  ds_clear_day  ds_fog_sun_day  ds_heavy_rain_day_night 	 ds_heavy_snow_day_night��%�  &	        &	 1     &	 l     &	 �     &	 �     &	     &	 X    &	 �    &	 �    &		     �� 5   
   $ ./Pictures/fair_day.png?�6'   �� 5   
   $' !./Pictures/Temperaturi/temp20.png?�6%   �� 5   
   $' !./Pictures/Temperaturi/temp21.png?�6%   �� 5   
   $' !./Pictures/Temperaturi/temp24.png?�6%   �� 5   
   $' !./Pictures/Temperaturi/temp30.png?�6%   �� 5   
   $' !./Pictures/Temperaturi/temp40.png?�6%   �� 5   
   $$ ./Pictures/ds/ds_clear_day.png?�6+   �� 5   
   $&  ./Pictures/ds/ds_fog_sun_day.png?�6-   �� 5   
   $/ )./Pictures/ds/ds_heavy_rain_day_night.png?�66   �� 5   
   $/ )./Pictures/ds/ds_heavy_snow_day_night.png?�66   5      .��5      �  � RowDefinitions 5   
   �� 5      $��2* �6   �� 5       $��2* �6   �� 5!      $��2* �6   �� 5"      $��2* �6   �� 5#      $��2* �6   �� 5$      $��2* �6   .+�5'   
   � $��2��6   $��2��6    � ColumnDefinitions 5(      �� 5)      $��1* �6#   �� 5*      $��1* �6#   .+�5-      �� -   5         ��Name$ Current_Day_Image��5-      $��2��6/   $��0��6<   #��[  6L   �� 5.      -   5        $ Current_Temp_Image��5.      $��1��60   $��60��6@   $��60��6L   #��[ 6W   50      � 52   
   $��3��6   $��2��6    54      �� 55      $��1* �6#   �� 56      $��1* �6#   �� 57      $��1* �6#   �� 58      $��1* �6#   �� 59      $��1* �6#    5<      �� 5=      $��1* �6    �� 5>      $��2* �6    �� 5?      $��2* �6    .+�5B      �� $��1��6   $��0��6!   
�������$	��Min��6D   $��Center=�6R   $��Center=�6o   �� 5C      $��1��6   $��1��6!   
�������$	��Max��6D   $��Center=�6R   $��Center=�6o   �� 5D      $��1��6   $��2��6!   
�������$	��Hum��6D   $��Center=�6R   $��Center=�6o   �� 5E      $��1��6   $��3��6!   
�������$��Wind dir��6D   $��Center=�6W   $��Center=�6t   �� 5F      $��1��6   $��4��6!   
�������$��
Wind speed��6D   $��Center=�6Y   $��Center=�6v   �� 5H      -   5         ��Name$ Current_Temp_Min��5H      $��2��6.   $��0��6;   
�������$	��...��6^   $��Center=�6l   $��Center=�6�   �� 5I      -   5        $ Current_Temp_Max��5I      $��2��6.   $��1��6;   
�������$	��...��6^   $��Center=�6l   $��Center=�6�   �� 5J      -   5        $ Current_Humidity��5J      $��2��6.   $��2��6;   
�������$	��...��6^   $��Center=�6l   $��Center=�6�   �� 5K      -   5        $ Current_Wind��5K      $��2��6*   $��3��67   
�������$	��...��6Z   $��Center=�6h   $��Center=�6�   �� 5L      -   5        $ Current_Wind_Speed��5L      $��2��60   $��4��6=   
�������$	��...��6`   $��Center=�6n   $��Center=�6�   5N      � 5P   
   $��4��6   $��2��6    5R      �� 5S      $��1* �6    �� 5T      $��1* �6    �� 5U      $��1* �6     5X      �� 5Y      $��2* �6#   �� 5Z      $��1* �6#   �� 5[      $��1* �6#   �� 5\      $��1* �6#   .+�5_      �� -   5        $ 
Next_day_1��5_      $��1��6(   $	��...��65   
�������$��Center=�6V   $��Center=�6s   $��	10,0,58,0q�6�   $	��124��6�   $��2��6�   �� 5`      -	   5        $ Next_day_1_Image��5`      $��1��6/   $��1��6<   #��[ 6L   �� 5a      -
   5        $ Next_day_1_Temp_Max��5a      $��1��61   $��2��6>   #��[ 6N   �� 5b      -   5        $ Next_day_1_Temp_Min��5b      $��1��61   $��3��6>   #��[ 6N   �� 5d      -   5        $ 
Next_day_2��5d      $��2��6(   $	��...��65   
�������$��Center=�6V   $��Center=�6s   $��	10,0,58,0q�6�   $	��124��6�   $��2��6�   �� 5e      -   5        $ Next_day_2_Image��5e      $��2��6.   $��1��6;   #��[ 6K   �� 5f      -   5        $ Next_day_2_Temp_Max��5f      $��2��61   $��2��6>   #��[ 6N   �� 5g      -   5        $ Next_day_2_Temp_Min��5g      $��2��61   $��3��6>   #��[ 6N   5i      � 5k   
   $��5��6   $��2��6    5m      �� 5n      $��1* �6    �� 5o      $��1* �6    �� 5p      $��1* �6     5s      �� 5t      $��2* �6#   �� 5u      $��1* �6#   �� 5v      $��1* �6#   �� 5w      $��1* �6#   .+�5z      �� -   5        $ 
Next_day_3��5z      $��0��6(   $	��...��65   
�������$��Center=�6V   $��Center=�6s   $��	10,0,58,0q�6�   $	��124��6�   $��2��6�   �� 5{      -   5        $ Next_day_3_Image��5{      $��0��6.   $��1��6;   #��[ 6K   �� 5|      -   5        $ Next_day_3_Temp_Max��5|      $��0��61   $��2��6>   #��[ 6N   �� 5}      -   5        $ Next_day_3_Temp_Min��5}      $��0��61   $��3��6>   #��[ 6N   �� 5      -   5        $ 
Next_day_4��5      $��1��6(   $	��...��65   
�������$��Center=�6V   $��Center=�6s   $��	10,0,58,0q�6�   $	��124��6�   $��2��6�   �� 5�      -   5        $ Next_day_4_Image��5�      $��1��6.   $��1��6;   #��[	 6K   �� 5�      -   5        $ Next_day_4_Temp_Max��5�      $��1��61   $��2��6>   #��[ 6N   �� 5�      -   5        $ Next_day_4_Temp_Min��5�      $��1��61   $��3��6>   #��[ 6N   5�      �� 5�   
   -   5        $
 City��5�      $��	Bucharest��6   
�������$��50(�6E   $��10,42,10,44q�6S   $	��300��6h   $��2��6t   &   System.Windows.Media.TextOptions   TextHintingMode$ Fixed=�6�   	   TextFormattingMode$	 Display=�6�   $��Center=�6�   $��Center=�6�   $��2��6  �� 5�   
   -   5        $ Current_Date��5�      $	��...��6&   
�������$��Center=�6H   $��Center=�6l   $��145,0,10,52q�6�   
 J� RenderTransformOrigin$
 0.507,0.551&�6�   �� 5�   
   -   5        $ Current_Status��5�      $	��...��6(   
�������$��Center=�6J   $��Center=�6n   $��	0,10,0,76q�6�   $��1��6�   $��2��6�   �� 5�   
   -   5        $ Current_Time��5�      $	��...��6&   
�������$��Center=�6H   $��Center=�6l   $��
0,0,175,52q�6�   5�      5�      