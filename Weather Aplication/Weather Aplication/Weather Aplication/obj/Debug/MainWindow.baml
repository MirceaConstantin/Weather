   M S B A M L   `   `   `  ����O  Kmscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e0891&clr-namespace:System;assembly=mscorlibSystem  5   	   M IWeather Aplication, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null7 clr-namespace:Weather_AplicationWeather_Aplication 5   	   #   Weather_Aplication.MainWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   6clr&clr-namespace:System;assembly=mscorlib     5   	   2local clr-namespace:Weather_Aplication     5   	     � Title$  
MainWindow��5	   	   $	��568��6   $	��320��6)    � AllowsTransparency .  � WindowStyle$
 None=�6O   ��6b   Z�  � 	Resources 5         clear_n �� 	UriSource  clear_d  cloudy_n  cloudy_d  -  x  i 
 return  app_icon��%*  &	        &	 <     &	 x     &	 �     &	 �     &	     &	 F    &	 p    &	 �    �� 5   
   $( "./Pictures/Backgrounds/clear_n.jpg?�6&   �� 5   
   $( "./Pictures/Backgrounds/clear_d.jpg?�6&   �� 5   
   $) #./Pictures/Backgrounds/cloudy_n.jpg?�6'   �� 5   
   $) #./Pictures/Backgrounds/cloudy_d.jpg?�6'   �� 5   
   $ ./Pictures/-.png?�6    �� 5   
   $ ./Pictures/x.png?�6    �� 5   
   $ ./Pictures/i.png?�6    �� 5   
   $ ./Pictures/return.png?�6%   �� 5   
   $ ./Pictures/app_icon.png?�6'   5      .��5      �  � RowDefinitions 5   
   �� 5      $��30 �6   �� 5      $	��538 �6   ��5   
   �� 5      -   5        
back_image�� �� ImageSource# [  5   -    �� Opacity$ 1Q�6`   .+�5"   
   � $��0��6   .+�5$      �� -   5        $
��Left=�5$      $��30��63   $	��Top=�6?   $	��320��6W   $��2��6c    J� RenderTransformOrigin$ 0.601,0.558&�6w   ���	#7F142B326�   �� 5&      -   5        $��20��5&      $��20��6!   $��	291,0,0,0q�6-   ���	#00DDDDDD���	#00707070���	#00000000.��5'      �� .+�5(      �� #��[ 6   $ 0.5,0.5&�6D   5)      5*      �� 5,      -   5        $��20��5,      $��20��6!   $��	241,0,0,0q�6,   ���	#00DDDDDD���	#00707070���	#00000000.��5-      �� .+�5.      �� #��[ 6   $ 0.463,0.477&�6D   5/      50      �� 52      -   5        	 ��Name$	 Info_but��52      $��20��6'   $��20��63   $��	191,0,0,0q�6>   ���	#00DDDDDD���	#00707070���	#00000000.��53      �� .+�54      �� #��[ 6   $ 0.463,0.477&�6D   55      56      �� 58      -   5        $	 
Return_but��58      $��20��6)   $��20��65   $��	191,0,0,0q�6@   ���	#00DDDDDD���	#00707070���	#00000000$ 0.514,0.535&�6�   .��59      �� .+�5:      �� #��[ 6   5;      5<      �� 5>      -   5        $��Weather App��5>      $
��Left=�6+   $��Center=�6M   
�������$��15(�6�   $��	30,0,80,0q�6�   �� 5@      -   5        $��20��5@      $��20��6!   #��[ 6,   $��
10,6,290,5q�6p   5B       � 5C   
   -	   5        
  �Name$

 Main��5C      $��1��6     � NavigationUIVisibility$ Hidden=�6+   5E      5F      