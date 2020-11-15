package courierServiceSystem;

import java.util.*;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.io.*;


public class CourierSystem {

public static void staffInfoEntry() { 
		
		JFrame f = new JFrame("Courier Service System");
		JLabel l1, l2, l3, l4, l5, l6, l7, l8, l9, l10;
		JTextField t1, t2, t3, t4, t5, t6;
		JComboBox j1, j2;
		JButton b1, b2, b3, b4;
		
		l7 = new JLabel("Employee's Details");
		l7.setBounds(170, 2, 150, 50);
		
		l1 = new JLabel(" Name* : ");
		l1.setBounds(50, 40, 120, 50);
		
		l2 = new JLabel(" Email ID* : ");
		l2.setBounds(50, 60, 140, 80);
		
		l3 = new JLabel("Father's name : ");
		l3.setBounds(50, 80, 120, 110);
		
		l4 = new JLabel("Mother's name : ");
		l4.setBounds(50, 100, 120, 140);
		
		l5 = new JLabel("Mobile No.* : ");
		l5.setBounds(50, 120, 120, 170);
		
		l6 = new JLabel("Martial Status : ");
		l6.setBounds(50, 140, 120, 200);
		
		l9 = new JLabel("Employee Type* : ");
		l9.setBounds(50, 160, 120, 230);
		
		l10 = new JLabel("Employee code(M/D/C-001(eg))* : ");
		l10.setBounds(5, 180, 180, 260);
		
		l8 = new JLabel("Note : This page is meant for enter and save new Data of Managing Staff, Delivery Staff an.");
		l8.setBounds(10, 400, 500, 30);		
		
		t1 = new JTextField();
		t1.setBounds(180, 55, 170, 25);
		
		t2 = new JTextField();
		t2.setBounds(180, 90, 170, 25);
		
		t3 = new JTextField();
		t3.setBounds(180, 125, 170, 25);
		
		t4 = new JTextField();
		t4.setBounds(180, 160, 170, 25);
		
		t5 = new JTextField();
		t5.setBounds(180, 195, 170, 25);
		
		t6 = new JTextField();
		t6.setBounds(180, 300, 170, 25);
		
		
		String s1[] = { " ", "Married", "Unmarried", "Divorced", "Widowed" };
		
		String s2[] = { " ", "Managing Staff", "Delivery Staff" };
		
		
		j1 = new JComboBox(s1);
		j1.setBounds(180, 230, 170, 25);
		
		j2 = new JComboBox(s2);
		j2.setBounds(180, 265, 170, 25);
		
		b1 = new JButton("Save");
		b1.setBounds(380, 50, 70, 30);
		
		b2 = new JButton("close");
		b2.setBounds(380, 90, 70, 30);
		
		b3 = new JButton("Reset");
		b3.setBounds(380, 130, 70, 30);
		
		b4 = new JButton("back");
		b4.setBounds(380, 170, 70, 30);
		
		
		b1.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				
				String s1 = t1.getText();
				String s2 = t2.getText();
				String s3 = t3.getText();
				String s4 = t4.getText();
				String s5 = t5.getText();
				String s8 = t6.getText();
				String s6 = j1.getSelectedItem() + " ";
				String s7 = j2.getSelectedItem() + " ";
				
				if(e.getSource() == b1) { 
					
					try { 
						String File_N = t6.getText() + ".txt";
						File_N.trim();
						File mfile = new File(File_N);
						FileWriter w = new FileWriter(File_N);
						
						w.write("Employee's name : " + s1 + "\n");
						w.write("Employee's Email ID : " + s2 + "\n");
						w.write("Employee's Father's name : " + s3 + "\n");
						w.write("Employee's Mother's name : " + s4 + "\n");
						w.write("Employee's Mob : " + s5 + "\n");
						w.write("Employee's Martial Status : " + s6 + "\n");
						w.write("Employee type : " + s7 + "\n");
						w.write("Employee Code : " + s8 + "\n");
						w.write("\n\n");
						w.close();
						
					} catch(Exception ae) { 
						System.out.println(ae);
					}
					
				}
				JOptionPane.showMessageDialog(f, "Successfully Saved" + " The Details");
				t1.setText(null);
				t2.setText(null);
				t3.setText(null);
				t4.setText(null);
				t5.setText(null);
				t6.setText(null);
				j1.setSelectedIndex(0);
				j2.setSelectedIndex(0);
			}
		});
		
		b2.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				
				f.dispose();
				
			}
		});
		
		b3.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				t1.setText(null);
				t2.setText(null);
				t3.setText(null);
				t4.setText(null);
				t5.setText(null);
				t6.setText(null);
				j1.setSelectedIndex(0);
				j2.setSelectedIndex(0);
				
			}
		});
		
		b4.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				
				CSSmanagingmenu();
				f.dispose();
			}
		});
		
		f.addWindowListener(new WindowListener() {
			
			@Override
			public void windowClosing(WindowEvent e) {
				
				System.exit(0);
				
			}

			@Override
			public void windowOpened(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}

			@Override
			public void windowClosed(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}

			@Override
			public void windowIconified(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}

			@Override
			public void windowDeiconified(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}

			@Override
			public void windowActivated(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}

			@Override
			public void windowDeactivated(WindowEvent e) {
				// TODO Auto-generated method stub
				
			}
			
		});
		
		f.add(l1);
		f.add(t1);
		f.add(l2);
		f.add(t2);
		f.add(l3);
		f.add(j1);
		f.add(j2);
		f.add(l4);
		f.add(l5);
		f.add(t3);
		f.add(l6);
		f.add(l7);
		f.add(l8);
		f.add(l9);
		f.add(l10);
		f.add(t6);
		f.add(b1);
		f.add(b2);
		f.add(b4);
		f.add(t4);
		f.add(t5);
		f.add(b3);
		f.setLayout(null);
		f.setSize(500, 500);
		f.setVisible(true);
	}
	
	static void loginScreen() { 
		
		JFrame f = new JFrame("Courier Service System");
		JLabel l1, l2, User_label, Pass_label;
		JTextField User_N;
		JPasswordField Passwrd;
		JButton login, reset, back;
		
		l1 = new JLabel("<html>" + "<font size='4' color='black'><u><strong>Welcome to courier Service System</strong></u></font>");
		l1.setBounds(70, 35, 300, 25);
		
		l2 = new JLabel("PLease Login to continue : ");
		l2.setBounds(40, 100, 250, 25);
		
		User_label = new JLabel("User name : ");
		User_label.setBounds(30, 160, 100, 25);
		
		Pass_label = new JLabel("Password : ");
		Pass_label.setBounds(30, 190, 100, 25);
		
		
		User_N = new JTextField();
		User_N.setBounds(130, 160, 150, 25);
		
		Passwrd = new JPasswordField();
		Passwrd.setBounds(130, 190, 150, 25);
		
		
		login = new JButton("Login");
		login.setBounds(140, 240, 70, 30);
		
		reset = new JButton("Reset");
		reset.setBounds(230, 240, 70, 30);
		
		back = new JButton("back");
		back.setBounds(270, 320, 70, 30);
		
		login.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				String username = User_N.getText();
				String password = Passwrd.getText();
				
				if(username.trim().equals("Admin") && password.trim().equals("Admin")) { 
					CSSmanagingmenu();
					f.dispose();
				} else { 
					JOptionPane.showMessageDialog(f, "Invalid User");
				}
				
			}
		});
		
		reset.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				User_N.setText(null);
				Passwrd.setText(null);
				
			}
		});
		
		back.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				Welcome_scr();
				f.dispose();
			}
		});
		
		f.add(l1);
		f.add(l2);
		f.add(User_label);
		f.add(Pass_label);
		f.add(User_N);
		f.add(Passwrd);
		f.add(login);
		f.add(reset);
		f.add(back);
		f.setLayout(null);
		f.setSize(400, 400);
		f.setVisible(true);
		
	}

	static void CSSmanagingmenu() { 
		
		JFrame f = new JFrame("Courier Service System");
		JLabel l1;
		JButton b1, b2, b3, b4, b5;
		
		l1 = new JLabel("CSS Managing Employee's Menu");
		l1.setBounds(180, 50, 200, 25);
		
		b1 = new JButton("Add");
		b1.setBounds(90, 120, 100, 25);
		
		b2 = new JButton("Delete");
		b2.setBounds(300, 120, 100, 25);
		
		b3 = new JButton("Search");
		b3.setBounds(90, 160, 100, 25);
		
		b4 = new JButton("Update");
		b4.setBounds(300, 160, 100, 25);
		
		b5 = new JButton("Go Back to login Page");
		b5.setBounds(120, 250, 250, 25);
		
		b1.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				staffInfoEntry();
				f.dispose();
			}
		});
		
		b2.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				emdelete();
				f.dispose();
			}
		});
		
		f.setDefaultCloseOperation(f.DISPOSE_ON_CLOSE);
		
		b3.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				EmSearch();
				f.dispose();
				
			}
		});
		
		
		
		b5.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				loginScreen();
				f.dispose();	
			}
		});
		
		f.add(l1);
		f.add(b1);
		f.add(b2);
		f.add(b3);
		f.add(b4);
		f.add(b5);
		f.setLayout(null);
		f.setSize(500,500);
		f.setVisible(true);
		
	}
	
	static void EmSearch() { 
		
		JFrame f = new JFrame("Courier Service System");
		JLabel l1, l2, l3;
		JButton b1, b2, b3;
		JTextField t1, t2;
		
		l1 = new JLabel("Fill the required fields to search : ");
		l1.setBounds(30, 50, 250, 25);
	
		l2 = new JLabel("Employee's name : ");
		l2.setBounds(30, 90, 250, 25);
		
		l3 = new JLabel("Employee Code : ");
		l3.setBounds(30, 120, 250, 25);
		
		t1 = new JTextField();
		t1.setBounds(140, 90, 250, 25);
		
		t2 = new JTextField();
		t2.setBounds(140, 120, 250, 25);
				
		b1 = new JButton("Search");
		b1.setBounds(140, 160, 100, 25);
		
		b2 = new JButton("Reset");
		b2.setBounds(290, 160, 100, 25);
		
		b3 = new JButton("Go Back to Main Menu");
		b3.setBounds(260, 230, 180, 25);
		
		b1.addActionListener(new ActionListener() {
			String data = " ";
			String data1 = " \n";
			@Override
			public void actionPerformed(ActionEvent e) {
				 try {
						String emp_name = t2.getText();
						String File_name = emp_name + ".txt";
						File_name.trim();
						
						File f = new File(File_name);
						
						if(f.exists()) { 
							
							Scanner myReader = new Scanner(f);
							while(myReader.hasNextLine()) { 
								
								data = myReader.nextLine();
								data1 = data1 + data + "\n";
								
							}
							JOptionPane.showMessageDialog(null, data1);
							data1 = " ";
							myReader.close();
							
						} else { 
							l1.setText("ouch");
						}
				 }catch(IOException ae) { 
					 System.out.println(ae);
				 }	
				
			}
		});
		
		
		b2.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				t1.setText(null);
				t2.setText(null);
				
			}
		});
		
		b3.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				CSSmanagingmenu();
				f.dispose();
				
			}
		});
		
		f.add(l1);
		f.add(l2);
		f.add(l3);
		f.add(t1);
		f.add(t2);
		f.add(b1);
		f.add(b2);
		f.add(b3);
		f.setLayout(null);
		f.setSize(500,500);
		f.setVisible(true);
	}
	
	static void emdelete() { 
		
		JFrame f = new JFrame("Courier Service System");
		JLabel l1, l2, l3;
		JButton b1, b2, b3;
		JTextField t1, t2;
		
		l1 = new JLabel("Fill the required fields to search : ");
		l1.setBounds(30, 50, 250, 25);
	
		l2 = new JLabel("Employee's name : ");
		l2.setBounds(30, 90, 250, 25);
		
		l3 = new JLabel("Employee Code : ");
		l3.setBounds(30, 120, 250, 25);
		
		t1 = new JTextField();
		t1.setBounds(140, 90, 250, 25);
		
		t2 = new JTextField();
		t2.setBounds(140, 120, 250, 25);
				
		b1 = new JButton("Delete");
		b1.setBounds(140, 160, 100, 25);
		
		b2 = new JButton("Reset");
		b2.setBounds(290, 160, 100, 25);
		
		b3 = new JButton("Go Back to Main Menu");
		b3.setBounds(260, 230, 180, 25);
		
		b1.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				
						String emp_name = t2.getText();
						String File_name = emp_name + ".txt";
						File_name.trim();
						
						File f = new File(File_name);
						
						if(f.delete()) { 
							JOptionPane.showMessageDialog(null, "Employee Data deleted!!!");
						} else { 
							JOptionPane.showMessageDialog(null, "Employee not found!!!");
						}
						t1.setText(null);
						t2.setText(null);
				
			}
		});
		
		
		b2.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				t1.setText(null);
				t2.setText(null);
				
			}
		});
		
		b3.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				CSSmanagingmenu();
				f.dispose();
				
			}
		});
		
		f.add(l1);
		f.add(l2);
		f.add(l3);
		f.add(t1);
		f.add(t2);
		f.add(b1);
		f.add(b2);
		f.add(b3);
		f.setLayout(null);
		f.setSize(500,500);
		f.setVisible(true);
		
	} 
	
	static void Welcome_scr() {
		
		JFrame f = new JFrame("Courier Service System");
		JLabel l1, l2;
		JButton b1, b2;
		
		l1 = new JLabel("<html>" + "<font size='4' color='black'><u><strong>Welcome to courier Service System</strong></u></font>");
		l1.setBounds(50, 20, 300, 30);
		
		l2 = new JLabel("Please Choose to Proceed : ");
		l2.setBounds(40, 90, 300, 30);
		
		b1 = new JButton("Managing Staff");
		b1.setBounds(70, 140, 150, 50);
		
		b2 = new JButton("Delivery Staff");
		b2.setBounds(70, 200, 150, 50);
		
		b1.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				loginScreen();
				f.dispose();
				
			}
		});
		
		b2.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				CSSDeliverymenu();
				f.dispose();
				
			}
		});
		
		f.add(l1);
		f.add(l2);
		f.add(b1);
		f.add(b2);
		f.setLayout(null);
		f.setSize(400, 400);
		f.setVisible(true);
		
	}
	
	
static void CSSDeliverymenu() { 
		
		JFrame f = new JFrame("Courier Service System");
		JLabel l1;
		JButton b1, b2, b3, b4, b5;
		
		l1 = new JLabel("CSS Delivery Employee's Menu");
		l1.setBounds(150, 50, 200, 25);
		
		b1 = new JButton("Edit");
		b1.setBounds(90, 120, 100, 25);
		
		b2 = new JButton("view Rating");
		b2.setBounds(300, 120, 100, 25);
		
		b3 = new JButton("Update Status");
		b3.setBounds(170, 160, 150, 25);
		
		b5 = new JButton("Go Back to login Page");
		b5.setBounds(120, 250, 250, 25);
		
		b1.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				
				f.dispose();
			}
		});
		
		b2.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				
				f.dispose();
			}
		});
		
		f.setDefaultCloseOperation(f.DISPOSE_ON_CLOSE);
		
		b3.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				JOptionPane.showMessageDialog(null, "Dear Customer.....Thank you for choosing our service " + "\n Acknowledgement Sent");
				
			}
		});
		
		
		
		b5.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				Welcome_scr();
				f.dispose();	
			}
		});
		
		f.add(l1);
		f.add(b1);
		f.add(b2);
		f.add(b3);
		
		f.add(b5);
		f.setLayout(null);
		f.setSize(500,500);
		f.setVisible(true);
		
	}
	
	public static void main(String[] args) {
		
		Welcome_scr();
	}

	
}
	