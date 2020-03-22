package com.example.commplus;

import android.app.Fragment;
import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;


/**
 * A simple {@link Fragment} subclass.
 */
public class QuickButtons extends Fragment {
    View view;
    Button button_back;
    Button button_top;
    Button button_reset;
    Button button_keyboard;

    public QuickButtons() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        view = inflater.inflate(R.layout.fragment_quick_buttons, container, false);

        button_back = (Button) view.findViewById(R.id.button_back);
        button_back.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                MainActivity main_activity = (MainActivity) getActivity();
                main_activity.sentence_bar_delete();
                main_activity.sentence_bar_write();
                FragmentManager fm = getFragmentManager();
                fm.popBackStackImmediate();
            }
        });

        button_top = (Button) view.findViewById(R.id.button_top);
        button_top.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                MainActivity main_activity = (MainActivity) getActivity();
                FragmentManager fm = getFragmentManager();
                for(int i = 0; i < fm.getBackStackEntryCount(); i++) {
                    fm.popBackStack();
                }
            }
        });

        button_reset = (Button) view.findViewById(R.id.button_reset);
        button_reset.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                MainActivity main_activity = (MainActivity) getActivity();
                main_activity.sentence_bar_clear();
                main_activity.sentence_bar_write();
                FragmentManager fm = getFragmentManager();
                for(int i = 0; i < fm.getBackStackEntryCount(); i++) {
                    fm.popBackStack();
                }
            }
        });

        button_keyboard = (Button) view.findViewById(R.id.button_keyboard);
        button_keyboard.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                MainActivity main_activity = (MainActivity) getActivity();
                InputMethodManager imm = (InputMethodManager) main_activity.getSystemService(Context.INPUT_METHOD_SERVICE);
                imm.toggleSoftInput(InputMethodManager.SHOW_FORCED, 0);
            }
        });

        return view;
    }
}
