import os

# 既存のlibディレクトリをベースディレクトリとして設定
base_dir = 'lib/'

# フォルダ構造の定義
folders = [
    'models',
    'viewmodels',
    'views',
    'services',
    'widgets',
    'utils'
]

# 各ファイルとその初期内容の定義
files = {
    'main.dart': """import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'viewmodels/auth_viewmodel.dart';
import 'views/auth_view.dart';

void main() {
  runApp(InstaCloneApp());
}

class InstaCloneApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthViewModel()),
        // 他のViewModelもここでプロバイダに追加
      ],
      child: MaterialApp(
        title: 'InstaClone',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: AuthView(),
      ),
    );
  }
}
""",

    'models/post.dart': """class Post {
  final String id;
  final String userId;
  final String imageUrl;
  final String caption;
  final DateTime createdAt;

  Post({
    required this.id,
    required this.userId,
    required this.imageUrl,
    required this.caption,
    required this.createdAt,
  });

  // FirestoreドキュメントからPostインスタンスを生成するメソッド
  factory Post.fromDocument(Map<String, dynamic> doc) {
    // TimestampからDateTimeに変換するために型キャストを使用
    return Post(
      id: doc['id'] as String,
      userId: doc['userId'] as String,
      imageUrl: doc['imageUrl'] as String,
      caption: doc['caption'] as String,
      createdAt: (doc['createdAt'] as Timestamp).toDate(),
    );
  }
}
""",

    'models/user.dart': """class User {
  final String id;
  final String email;
  final String username;
  final String profileImageUrl;

  User({
    required this.id,
    required this.email,
    required this.username,
    required this.profileImageUrl,
  });

  // FirestoreドキュメントからUserインスタンスを生成するメソッド
  factory User.fromDocument(Map<String, dynamic> doc) {
    return User(
      id: doc['id'] as String,
      email: doc['email'] as String,
      username: doc['username'] as String,
      profileImageUrl: doc['profileImageUrl'] as String,
    );
  }
}
""",

    'viewmodels/auth_viewmodel.dart': """import 'package:flutter/material.dart';

class AuthViewModel extends ChangeNotifier {
  // 認証に関連するロジックをここに記述
}
""",

    'viewmodels/post_viewmodel.dart': """import 'package:flutter/material.dart';

class PostViewModel extends ChangeNotifier {
  // 投稿に関連するロジックをここに記述
}
""",

    'viewmodels/feed_viewmodel.dart': """import 'package:flutter/material.dart';

class FeedViewModel extends ChangeNotifier {
  // フィード表示に関連するロジックをここに記述
}
""",

    'views/auth_view.dart': """import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../viewmodels/auth_viewmodel.dart';

class AuthView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final authViewModel = Provider.of<AuthViewModel>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text('Auth View'),
      ),
      body: Center(
        child: Text('Auth View Content'),
      ),
    );
  }
}
""",

    'views/post_view.dart': """import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../viewmodels/post_viewmodel.dart';

class PostView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final postViewModel = Provider.of<PostViewModel>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text('Post View'),
      ),
      body: Center(
        child: Text('Post View Content'),
      ),
    );
  }
}
""",

    'views/feed_view.dart': """import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../viewmodels/feed_viewmodel.dart';

class FeedView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final feedViewModel = Provider.of<FeedViewModel>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text('Feed View'),
      ),
      body: Center(
        child: Text('Feed View Content'),
      ),
    );
  }
}
""",

    'services/auth_service.dart': """class AuthService {
  // Firebase Authentication に関連するサービスの実装
  // 例: サインイン、サインアップ、サインアウトなどのメソッド
}
""",

    'services/firestore_service.dart': """class FirestoreService {
  // Firestore データベース操作に関連するサービスの実装
  // 例: ドキュメントの追加、更新、削除、取得などのメソッド
}
""",

    'services/storage_service.dart': """class StorageService {
  // Firebase Storage に関連するサービスの実装
  // 例: ファイルのアップロード、ダウンロードなどのメソッド
}
""",

    'widgets/post_card.dart': """import 'package:flutter/material.dart';

class PostCard extends StatelessWidget {
  final String imageUrl;
  final String caption;

  PostCard({required this.imageUrl, required this.caption});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Column(
        children: [
          Image.network(imageUrl),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(caption),
          ),
        ],
      ),
    );
  }
}
""",

    'widgets/loading_indicator.dart': """import 'package:flutter/material.dart';

class LoadingIndicator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: CircularProgressIndicator(),
    );
  }
}
""",

    'utils/constants.dart': """const String appName = 'InstaClone';

// 他の定数をここに追加できます
"""
}

# ディレクトリとファイルの作成
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

for file_path, content in files.items():
    full_path = os.path.join(base_dir, file_path)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("libディレクトリ内のディレクトリとファイルの作成が完了しました。")