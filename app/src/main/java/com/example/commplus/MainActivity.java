package com.example.commplus;

import android.app.Fragment;
import android.app.FragmentTransaction;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentManager;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Begin the transaction
        FragmentTransaction ft = getFragmentManager().beginTransaction();
        // Add the contents of the container with the new fragment
        ft.add(R.id.fragment_container, new fragment0());
        // Complete the changes added above
        ft.commit();
    }

//    private void loadFragment(Fragment fragment) {
//        // create a FragmentManager
//        FragmentManager fm = getFragmentManager();
//        // create a FragmentTransaction to begin the transaction and replace the Fragment
//        FragmentTransaction fragmentTransaction = fm.beginTransaction();
//        // replace the FrameLayout with new Fragment
//        fragmentTransaction.replace(R.id.button_frame, fragment);
//        fragmentTransaction.commit(); // save the changes
//    }
}
