class Fragment:
    def __init__ (self, name, level, buttons):
        self.name = name;
        self.level = level;
        self.buttons = buttons;
        
pages = [];
pages.append(Fragment("Main", 0, ["Medical", "Social", "Emotional"]));
pages.append(Fragment("Social", 1, ["Work", "Family", "Friends", "Finance"]));


xml_relative_layout = '<?xml version="1.0" encoding="utf-8"?>\n<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"\n\txmlns:tools="http://schemas.android.com/tools"\n\tandroid:layout_width="match_parent"\n\tandroid:layout_height="match_parent" >\n';

## xml file generation
def create_xml (f):
    text = xml_relative_layout;
    text += '\t<LinearLayout\n\t\tandroid:layout_width="match_parent"\n\t\tandroid:layout_height="match_parent"\n\t\tandroid:layout_weight="1"\n\t\tandroid:orientation="horizontal"\n\t\tandroid:weightSum="' + str(len(f.buttons)) + '" >\n';

    for button in f.buttons:
        text += '\t\t<Button\n\t\t\tandroid:id="@+id/' + button.lower() + '"\n\t\t\tandroid:layout_width="0dp"\n\t\t\tandroid:layout_height="match_parent"\n\t\t\tandroid:layout_weight="1"\n\t\t\tandroid:scaleType="fitCenter"\n\t\t\tandroid:text="' + button + '" />\n';

    text += '\t</LinearLayout>\n';
    text += '</RelativeLayout>';
    return text;

java_imports = 'package com.example.commplus;\n\nimport android.app.Fragment;\nimport android.app.FragmentTransaction;\nimport android.os.Bundle;\nimport android.view.LayoutInflater;\nimport android.view.View;\nimport android.view.ViewGroup;\nimport android.widget.Button;';

## java file generation
def create_java (f):
    text = java_imports;
    text += '\n\npublic class fragment' + f.name + ' extends Fragment {';
    text += '\n\tView view;\n';
    
    for button in f.buttons:
        text += '\n\tButton ' + button.lower() + '_button;';
        
    text += '\n\t@Override\n\tpublic View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {';
    text += '\n\t\tview = inflater.inflate(R.layout.fragment_' + f.name.lower() + ', container, false);\n';

    for button in f.buttons:
        text += '\n\t\t' + button.lower() + '_button = (Button) view.findViewById(R.id.' + button.lower() + ');';
        text += '\n\t\t' + button.lower() + '_button.setOnClickListener(new View.OnClickListener() {';
        text += '\n\t\t\tpublic void onClick(View v) {'
        text += '\n\t\t\t\tFragmentTransaction ft = getFragmentManager().beginTransaction();';
        text += '\n\t\t\t\tft.replace(R.id.fragment_container, new fragment' + button + '());';
        text += '\n\t\t\t\tft.addToBackStack(null);';
        text += '\n\t\t\t\tft.commit();';
        text += '\n\t\t\t}\n\t\t});'

    text += '\n\n\t\t return view;\n\t}\n}';
    return text;

## generate xml files for all fragments
for page in pages:
    filename = "layouts/fragment_" + page.name.lower() + ".xml";
    file = open(filename, "w");
    file.write(create_xml(page));
    file.close();

## generate java files for all fragments
for page in pages:
    filename = "java/fragment" + page.name + ".java";
    file = open(filename, "w");
    file.write(create_java(page));
    file.close();
