{
  'variables': {
    'grit_dir': 'vendor/grit'
  },
  'targets': [
    {
      'target_name': 'pdf_viewer',
      'type': 'none',
      'actions': [
        {
          'action_name': 'pdf_viewer',
          'inputs': [
            'resources.grd',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/grit/pdf_viewer_resources.h',
            '<(SHARED_INTERMEDIATE_DIR)/grit/pdf_viewer_resources_map.cc',
            '<(SHARED_INTERMEDIATE_DIR)/grit/pdf_viewer_resources_map.h',
            '<(PRODUCT_DIR)/pdf_viewer_resources.pak',
          ],
          'action': [
            'python',
            '<(grit_dir)/grit.py',
            '-i',
            '<@(_inputs)',
            'build',
            '-o',
            '<(SHARED_INTERMEDIATE_DIR)/grit',
          ],
        }
      ],
    },  # target pdfviewer
  ],
}
