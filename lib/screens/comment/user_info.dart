import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class UserInfo extends StatelessWidget {
  final String userId;

  UserInfo({required this.userId});

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<DocumentSnapshot>(
      future: FirebaseFirestore.instance.collection('users').doc(userId).get(),
      builder: (context, snapshot) {
        if (!snapshot.hasData) {
          return Center(child: CircularProgressIndicator());
        }
        if (snapshot.hasError) {
          return Center(child: Text('エラー: ${snapshot.error}'));
        }
        final userData = snapshot.data!.data() as Map<String, dynamic>;
        final userProfileImage = userData['profileImageUrl'] ?? 'https://via.placeholder.com/150';
        final username = userData['username'] ?? 'Unknown';

        return Row(
          children: [
            CircleAvatar(
              backgroundImage: NetworkImage(userProfileImage),
            ),
            SizedBox(width: 8.0),
            Text(username),
          ],
        );
      },
    );
  }
}
